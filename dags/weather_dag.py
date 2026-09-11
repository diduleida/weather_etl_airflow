from airflow import DAG # клас DAG  (контейнер для всього  workflow)
from airflow.operators.python import PythonOperator # міст між Airflow і  Python-функцією
from sqlalchemy import create_engine, text # за допомогою нього ми будемо спілкуватися з бд
from datetime import datetime
from src.config import GEOCODING_URL, WEATHER_URL, API_KEY, DB_USER, DB_PASSWORD, DB_HOST,DB_PORT , DB_NAME
from src.extract import extract
from src.storage import save_raw, read_raw
from src.validation import validation
from src.transform import transform
from src.load import load


# ** - kwargs (keyword arguments) - довільна кількість аргументів можна отримати
# context - назва змінної, вона буде містити контекст поточного виконання тобто інфа про поточний запуск
# context створює Airflow під час запуску task, він знає купу інформації про поточне виконання
# ми типу кажемо візьми всі **keyword arguments, які передадуть, і збери їх у словник з назвою context
def extract_and_save (**context): 
    data = extract(
        GEOCODING_URL=GEOCODING_URL,
        WEATHER_URL=WEATHER_URL,
        API_KEY=API_KEY
    )
    batch_id = context['run_id'] # ця змінна має декілька значень (словник) і ми тут уточнюємо що нас цікавить
    filename = save_raw( # тут 
        data=data,
        batch_id=batch_id
    )
    return filename




def validate_raw(**context):
    filename = context['ti'].xcom_pull( # витягуємо конкретний екземпляр конкретної task у конкретному запуску DAG, ti (TaskInstance)  
        task_ids='extract_weather' # task_ids - назва параметра методу xcom_pull , ми йому кажемо що передаєио значення (extract_weather) в xcom_pull
    )
    data = read_raw(filename)
    validation(data)
    return filename



def transform_and_load(**context):
    filename = context['ti'].xcom_pull(
        task_ids='validate_weather'
    )
    data=read_raw(filename)
    df = transform(data)
    load(df)
    return f'{filename} loaded successfully!'


def load_weather():
        engine=create_engine(
        f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        )
        with open('/opt/airflow/sql/load/202_load_table_weather.sql','r') as file:
             sql = file.read()

        # engine — створює "точку входу" для підключення до БД
        # begin -  відкрий з'єднання з бд і почни транзакцію (робимо канал)
        # connection.execute() - виконати sql команду через з'єднання
        # sql - це той самий insert into
        # text -  обгортка для sql-рядка щоб його виконати
        with engine.begin() as connection:
             connection.execute(text(sql))


with DAG(
    # тут описуємо як поводитися з dag
    dag_id='weather_pipline', # ідентифікатор dag в Airflow, так будемо звертатися до нього і тд
    start_date=datetime(2026, 9, 1),
    schedule=None, # розклад як часто запускати і чи взагалі запускати
    catchup=False # чи робити пропушені запуски
) as dag: # назва всередині блоку, як Python називає об'єкт DAG, коли будемо звертатися до daga від python-коду
    # а тут опис роботи, з цим і як працювати
    extract_task = PythonOperator( # назва змінної в коді
        task_id='extract_weather', # це вже назва таски 
        python_callable=extract_and_save, # тут ми викликаємофункцію, яку самі написали вище або імпортували
    )
    validate_task = PythonOperator(
        task_id='validate_weather',
        python_callable=validate_raw
    )
    transform_and_load_task = PythonOperator(
        task_id='transform_and_load_to_db',
        python_callable=transform_and_load
    )
    load_weather_task = PythonOperator(
         task_id='load_weather',
         python_callable=load_weather
    )


    extract_task >> validate_task >> transform_and_load_task >> load_weather_task




