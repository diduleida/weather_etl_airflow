from sqlalchemy import create_engine # за допомогою нього ми будемо спілкуватися з бд
from .config import DB_USER, DB_PASSWORD, DB_HOST,DB_PORT , TABLE_NAME, DB_NAME


def load(df):
    # підключаємось до бд
    engine=create_engine(
        f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    df.to_sql(f'{TABLE_NAME}',engine, if_exists='append',index=False)