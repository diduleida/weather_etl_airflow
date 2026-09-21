from sqlalchemy import create_engine # за допомогою нього ми будемо спілкуватися з бд
from .db import engine
from .config import TABLE_NAME


def load(df):
    df.to_sql(f'{TABLE_NAME}',engine, if_exists='append',index=False)



