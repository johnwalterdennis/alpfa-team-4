import os
from utils import parse_resume, extract_keywords, match_jobs, pre_process
import streamlit as st

job_relevant_keywords = [
    "python", "machine learning", "data analysis", "flask", "django", "sql",
    "cloud", "api", "tensorflow", "pandas", "numpy","java","c#", "c++", "c", "linux","mysql", "postgresql",
    "rust","javascript", "ruby", "go", "typescript", "php", "html" "css", "node", "js",
    "git", "github", "spring", "pandas", "nosql", "mongodb", "aws", "azure", "nlp", "kotlin",
    "swift"
]


st.title('Candidate->Sponsor Match System')

# Testing to hold resumes here
RESUME_FOLDER = 'uploads'
# Make directory                PROBABLY GOING TO HAVE TO STORE THE RESUME IN THE DATABASE
if not os.path.exists(RESUME_FOLDER):
    os.makedirs(RESUME_FOLDER)

# Upload resume ui
st.header('Upload Your Resume')
question1 = st.text_area("What motivates you")
question2 = st.text_area("What are your hobbies")
question3 = st.text_area("Describe something challenging you have overcome")
uploaded_resume = st.file_uploader('Upload your resume (PDF)', type='pdf')

if st.button('Submit'):
    if uploaded_resume is not None:
        filename = os.path.join(RESUME_FOLDER, uploaded_resume.name)
        with open(filename, "wb") as destination:
            destination.write(uploaded_resume.getbuffer())


# Reads the resume and extracts the keywords
###################################
# NEED TO MODIFY KEYWORD EXTRACTION
##################################

    parsed_text = parse_resume(filename)
    cleaned_text = pre_process(parsed_text)

    # st.text_area('Parsed Resume Text', parsed_text)
    st.text_area('Cleaned Text', cleaned_text)

    keywords = extract_keywords(cleaned_text, job_relevant_keywords)
    st.write("Extracted Keywords: ", keywords)

    st.header('Job Matches')

    # Test jobs until we connect with database
    jobs = [
        {"title": "Software Engineer", "description": "Looking for someone with Python, Flask, SQL, Java, React"},
        {"title": "Data Scientist", "description": "C#, MongoDB, PostgreSQL, Java"}
    ]

    matched_jobs = match_jobs(keywords, jobs, job_relevant_keywords)


    for job, score in matched_jobs:
        st.write(f'Job: {job["title"]}, Match Score: {score}')

