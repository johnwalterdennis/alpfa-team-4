#database file and functions
from dotenv import load_dotenv
import os 
import pymysql

if load_dotenv() != True:
    print('no env file found')
    exit()


db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME') 

def create_connection():
    try:
        connection = pymysql.connect(
            host= db_host,
            user= db_user,
            password= db_pass,
            database= db_name
        ) 

        if connection:
            print('connection working')
            return connection

    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

create_connection()