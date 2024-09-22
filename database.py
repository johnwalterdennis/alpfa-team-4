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
        ) #using mymysql to connect to db

        if connection:
            print('connection working')
            return connection

    except pymysql.MySQLError as e:
        print(f"Could not connect to MySQL: {e}")
        return None

create_connection()
def insert_candidate(name, email, location, resume_text, keywords, sentiment_score, motivation, hobbies, challenges):
    connection = create_connection()
    if connection is None:
        return print(False)
    try:
        with connection.cursor() as cursor:#using a cursor object is also best practice
            sql = """
            INSERT INTO Candidates (name, email, location, resume_text, keywords, sentiment_score, motivation, hobbies, challenges)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            #apparently the %s place holder is good practice
            #this sql code block will be executed at query execution at cursor.execution(sql, values %s)
            print(f"Inserting: {name}, {email}, {location}, {resume_text}, {keywords}, {sentiment_score}, {motivation}, {hobbies}, {challenges}")
            cursor.execute(sql, (name, email, location, resume_text, keywords, sentiment_score, motivation, hobbies, challenges))#feeding the called parameters into the sql query
            connection.commit() #commit to db
            candidate_id = cursor.lastrowid #nice function that give us the id of the most recent entry
            return candidate_id
    except pymysql.MySQLError as e:
        print(f"Error inserting candidate: {e}") #error handling
        return None
    finally:
        connection.close()