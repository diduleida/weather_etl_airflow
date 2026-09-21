from airflow import DAG
from airflow.operators.python import PythonOperator
from sqlalchemy import  text 
from datetime import datetime
from src.db import engine


def load_daily():
    with open('/opt/airflow/sql/load/204_load_table_daily_weather.sql', 'r') as file:
        sql= file.read()

        with engine.begin() as connection:
            connection.execute(text(sql))


with DAG(
    dag_id='daily_weather',
    start_date=datetime(2026, 9, 19),
    schedule='@daily',
    catchup=False
) as dag:
    load_daily_weather_task=PythonOperator(
        task_id='load_daily_weather',
        python_callable=load_daily
    )

    load_daily_weather_task