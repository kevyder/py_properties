import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_SCHEMA = os.getenv("MYSQL_SCHEMA")
MYSQL_PORT = os.getenv("MYSQL_PORT")

try:
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_SCHEMA,
        port=MYSQL_PORT
    )

    if connection.is_connected():
        session = connection.cursor(dictionary=True)
        print("Connected to MySQL database")
except Error as e:
    print("Error while connecting to MySQL", e)
