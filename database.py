import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env.env')

DB_USER_RNIS_TO = os.getenv("DB_USER_RNIS_TO")
DB_PASSWORD_RNIS_TO = os.getenv("DB_PASSWORD_RNIS_TO")
DB_HOST_RNIS_TO = os.getenv("DB_HOST_RNIS_TO")
DB_PORT_RNIS_TO = os.getenv("DB_PORT_RNIS_TO")
DB_NAME_RNIS_TO = os.getenv("DB_NAME_RNIS_TO")
DB_USER_AV = os.getenv("DB_USER_AV")
DB_PASSWORD_AV = os.getenv("DB_PASSWORD_AV")
DB_HOST_AV = os.getenv("DB_HOST_AV")
DB_PORT_AV = os.getenv("DB_PORT_AV")
DB_NAME_AV = os.getenv("DB_NAME_AV")

def connect_db_rnis_to():
    connection = psycopg2.connect(user=DB_USER_RNIS_TO,
                                    password=DB_PASSWORD_RNIS_TO,
                                    host=DB_HOST_RNIS_TO,
                                    port=int(DB_PORT_RNIS_TO),
                                    database=DB_NAME_RNIS_TO)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return connection

def connect_db_avtovokzal():
    connection = psycopg2.connect(user=DB_USER_AV,
                                    password=DB_PASSWORD_AV,
                                    host=DB_HOST_AV,
                                    port=DB_PORT_AV,
                                    database=DB_NAME_AV)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return connection