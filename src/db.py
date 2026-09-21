from sqlalchemy import create_engine # за допомогою нього ми будемо спілкуватися з бд
from .config import DB_USER, DB_PASSWORD, DB_HOST,DB_PORT , TABLE_NAME, DB_NAME

engine=create_engine(
        f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )