from minio import Minio
import io
import json
from config import MINIO_ENDPOINT,MINIO_ACCESS_KEY,MINIO_SECRET_KEY, MINIO_BUCKET


# створюємо агента minIO
def get_minio_client():
    return  Minio(
        MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False # кажемо бібліотеці по якому протоколу підулючатися до minIO (http)
        )

# зберігаємо дані
def save_raw(data,batch_id):
    client = get_minio_client() # створюємо агента

    # перевіряємо чи існує наший бакет (true/false)
    found = client.bucket_exists(MINIO_BUCKET)
    if not found:
        client.make_bucket(MINIO_BUCKET)
    filename = f'{batch_id}.json' # назва файла
    # json.dumps() - перетворює py об'єкт в json рядок, utf-8 перетв в байти (бо put_object читає байти)
    json_bytes = json.dumps(data).encode('utf-8')
    # BytesIO створює  файлоподібний  об'єкт у пам'яті, put_object такий очікує
    data_stream = io.BytesIO(json_bytes)

    # завантажуємо в minIO
    client.put_object(
        bucket_name=MINIO_BUCKET,
        object_name=filename,
        data=data_stream,
        length=len(json_bytes), # скільки байтів треба завантажити
        content_type="application/json"# тип об'єкту який завантажуємо
    )
    print(f'{filename} saved successfully!')
