# load eviroment variable
from dotenv import load_dotenv
import os

# load mysql connector
import mysql.connector
from mysql.connector import Error

# check eviroment variable
# env_file = ".env.dev" if os.getenv("ENVIRONMENT") == "dev" else ".env.prod"

# load eviroment variable
load_dotenv()

# get value from eviroment variable
host = os.getenv("DB_HOST")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")
port = os.getenv("DB_PORT")

# print(host)
# print(user)


def connect():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        if connection.is_connected():
            # print("Connect to database successfully")
            return connection
    except Error as e:
        print(e)
        return None


# test connect
# connect()
