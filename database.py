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

def insert_candidate(name, email, location, resume_text, sentiment_score, motivation, hobbies, challenges):
    connection = create_connection()
    if connection is None:
        return print(False)
    try:
        with connection.cursor() as cursor:#using a cursor object is also best practice
            sql = """
            INSERT INTO Candidates (name, email, location, resume_text, sentiment_score, motivation, hobbies, challenges)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            #apparently the %s place holder is good practice
            #this sql code block will be executed at query execution at cursor.execution(sql, values %s)
            # print(f"Inserting: {name}, {email}, {location}, {resume_text}, {sentiment_score}, {motivation}, {hobbies}, {challenges}")
            cursor.execute(sql, (name, email, location, resume_text, sentiment_score, motivation, hobbies, challenges))#feeding the called parameters into the sql query 
            connection.commit() #commit to db
            candidate_id = cursor.lastrowid #nice function that give us the id of the most recent entry
            return candidate_id
    except pymysql.MySQLError as e:
        print(f"Error inserting candidate: {e}") #error handling
        return None
    finally:
        connection.close()

def insert_candidate_keywords(candidate_id, keywords_scores):
    """
    Inserts keywords and their scores for a candidate.

    Args:
        candidate_id (int): The ID of the candidate.
        keywords_scores (list): A list of tuples (keyword, score).
    """
    connection = create_connection()
    if connection is None:
        return False

    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Candidate_keywords (candidate_id, keyword, score)
            VALUES (%s, %s, %s)
            """
            data = [(candidate_id, keyword, score) for (keyword, score) in keywords_scores]
            cursor.executemany(sql, data)
            connection.commit()
            return True
    except pymysql.MySQLError as e:
        print(f"Error inserting candidate keywords: {e}")
        return False
    finally:
        connection.close()

def insert_sponsor(name, email, bio, keywords, password):
    connection = create_connection()
    if connection is None:
        return False
    
    try: 
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Sponsors (name, email, bio, keywords, password)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (name, email, bio, keywords, password))
            connection.commit()
            sponsor_id = cursor.lastrowid
            return sponsor_id
    except pymysql.MySQLError as e:
        print(f"Error inserting sponsor: {e}")
        return None
    finally: 
        connection.close


def insert_jobs(title, description, sponsor_id, keywords, personality, application_link):
    connection = create_connection()
    if connection is None:
        return False
    
    keyword_str = ','.join(map(str, keywords))
    
    print(keyword_str)

    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Job_postings (title, description, sponsor_id, keywords, personality, application_link)
            VALUES ( %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (title, description, sponsor_id, keyword_str, personality, application_link))
            connection.commit()
            job_posting_id = cursor.lastrowid
            return job_posting_id
    except pymysql.MySQLError as e:
        print(f"Error inserting sponsor: {e}")
        return None
    finally: 
        connection.close

def get_all_job_postings():
    """
    Retrieves all job postings from the database and returns a dictionary
    with job IDs as keys and lists of keywords as values.

    Returns:
        dict: A dictionary where each key is a job ID, and each value is a list of keywords.
    """
    connection = create_connection()
    if connection is None:
        return False

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # Select only the necessary fields
            sql = "SELECT id, keywords FROM Job_postings"
            cursor.execute(sql)
            job_postings = cursor.fetchall()

            # Initialize the dictionary to hold job IDs and keywords
            job_keywords_dict = {}

            for job in job_postings:
                job_id = job['id']
                keywords_str = job['keywords']
                if keywords_str:
                    # Assuming keywords are stored as a comma-separated string
                    keywords = [kw.strip() for kw in keywords_str.split(',')]
                else:
                    keywords = []
                job_keywords_dict[job_id] = keywords

            return job_keywords_dict
    except pymysql.MySQLError as e:
        print(f"Error retrieving job postings: {e}")
        return {}
    finally:
        connection.close()

def get_job_application_by_id(id):
    connection = create_connection()
    if connection is None:
        return None

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
            SELECT title, application_link FROM Job_postings
            WHERE id = %s
            """
            cursor.execute(sql, (id))
            application = cursor.fetchall()
            return application
    except pymysql.MySQLError as e:
        print(f"Error retrieving job application: {e}")
        return None
    finally:
        connection.close()
        