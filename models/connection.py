import os
from dotenv import load_dotenv
from mysql.connector import connect

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')


def connect_to_db():
    connection = None

    try:
        connection = connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database='pymarktime'
        )
    except Exception as err:
        print(f'Error al conectarse a la BBDD.{err}')

    return connection
