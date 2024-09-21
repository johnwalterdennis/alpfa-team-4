import streamlit as st
from utils import parse_resume, extract_keywords, match_jobs, pre_process


job_relevant_keywords = [
    "python", "machine learning", "data analysis", "flask", "django", "sql",
    "cloud", "api", "tensorflow", "numpy","java","c#", "c++", "c", "linux","mysql", "postgresql",
    "rust","javascript", "ruby", "go", "typescript", "php", "html" "css", "node", "js",
    "git", "github", "spring", "pandas", "nosql", "mongodb", "aws", "azure", "nlp", "kotlin",
    "swift", "golang"
]

st.title('Sponsor Upload Page')

# Stores Company Name
st.header('Company Name')

# Stores Company Location
st.header('Job Location')

# Stores skills and job description
st.header('Job Description')
job_description = st.text_area('Job Description')
if st.button('Submit'):
    if job_relevant_keywords is not None:
        cleaned_text = pre_process(job_description)
        st.write('Cleaned text: ', cleaned_text)

        keywords = extract_keywords(cleaned_text, job_relevant_keywords)
        st.write('Extracted Keywords ', keywords)


