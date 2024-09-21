import os
from parse_resume import parse_resume
from utils import parse_resume, extract_keywords, match_jobs, pre_process
import streamlit as st

job_relevant_keywords = [
    "python", "machine learning", "data analysis", "flask", "django", "sql",
    "cloud", "api", "tensorflow", "pandas", "numpy","java","c#", "c++", "c", "linux","mysql", "postgresql",
    "rust","javascript", "ruby", "go", "typescript", "php", "html" "css", "node", "js",
    "git", "github", "spring", "pandas", "nosql", "mongodb", "aws", "azure", "nlp", "kotlin",
    "swift"
]

<<<<<<< HEAD

st.title('Candidate-Sponsor Match System')
=======
# UI PART
st.title('Candidate->Sponsor Match System')
st.write("JOB ID : 102314")
st.write("Software Developer Role")
st.markdown("""
### Minimum Qualifications:
- Currently enrolled in an Associate, Bachelor's, or Master's degree program or post-secondary training in software development or a related technical field.
- Experience in software development.
- Experience coding in one or more of C, C++, Java, JavaScript, Python, or similar.

### Preferred Qualifications:
- Experience in web application development, Unix/Linux environments, mobile development, machine learning, and more.
- Experience with data structures and algorithms.
- Full-time availability for a minimum of 6 months.
- Ability to communicate fluently in English for complex technical discussions.

### About the Job:
As a Software Engineering Intern, you'll work on Google's core products and services, solving complex technical problems and collaborating on scalable solutions.

### Responsibilities:
- Develop scripts to automate routine tasks.
- Collaborate with peers and teams to innovate and solve problems.
- Apply knowledge gained in computer science to real-world challenges.
""")






# 
>>>>>>> 08e76e3574905ada11e32b62785f7de018ec5e01

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
uploaded_resume = st.file_uploader('Upload your resume (PDF) Limit: 5mb', type=['pdf', 'docx'])

# Limiting File size to 5MB function
# 5 MB in bytes
MAX_FILE_SIZE = 5 * 1024 * 1024

if uploaded_resume is not None:
    # Check file size
    if uploaded_resume.size > MAX_FILE_SIZE:
        st.error("File size exceeds the 5 MB limit. Please upload a smaller file.")
    else:
        st.success("File uploaded successfully!")
        st.write(f"File type: {uploaded_resume.type}")
        st.write(f"File size: {uploaded_resume.size / 1024:.2f} KB")

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
    # cleaned_text = pre_process(parsed_text)


    st.text_area('Parsed Resume Text: ', parsed_text)
    # st.text_area('Cleaned Text', cleaned_text)

    # keywords = extract_keywords(cleaned_text, job_relevant_keywords)
    # st.write("Extracted Keywords: ", keywords)

    # st.header('Job Matches')

    # # Test jobs until we connect with database
    # jobs = [
    #     {"title": "Software Engineer", "description": "Looking for someone with Python, Flask, SQL, Java, React"},
    #     {"title": "Data Scientist", "description": "C#, MongoDB, PostgreSQL, Java"}
    # ]

    # matched_jobs = match_jobs(keywords, jobs, job_relevant_keywords)


    # for job, score in matched_jobs:
    #     st.write(f'Job: {job["title"]}, Match Score: {score}')

