import os
from parse_resume import parse_resume
from keyword_extraction import compute_similar_keywords, extract_native_keywords
# from utils import match_jobs, pre_process
# from matching_algorithm import match_jobs
from database import insert_candidate, create_connection, insert_candidate_keywords, get_all_job_postings, get_job_application_by_id
from matching_algorithm import get_match
import streamlit as st

st.title('Candidate->Sponsor Match System')

# Testing to hold resumes here
RESUME_FOLDER = 'uploads'
# Make directory                PROBABLY GOING TO HAVE TO STORE THE RESUME IN THE DATABASE
if not os.path.exists(RESUME_FOLDER):
    os.makedirs(RESUME_FOLDER)

# Upload resume ui
st.header('Upload Your Resume')
userName= st.text_area("We encourage employees to take ownership of their projects and outcomes. Can you describe a time when you took the lead on a project and drove it to success?")
userEmail = st.text_area("How have you contributed to initiatives that have a positive impact on society, the environment, or your community?")
userLocation = st.text_area("Describe a time when you encountered a significant challenge at work. How did you approach resolving it?")
userMotivation = st.text_area("we put the client at the center of everything. How do you approach understanding and meeting the needs of clients?")
userHobbies = st.text_area("Can you share an example of how you went above and beyond for a client or customer, and what was the outcome?")
userChallanges = st.text_area("What motivates you to succeed in your professional life, and how does that align with the financial services industry?")
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

    parsed_text = parse_resume(filename)
    jobs = get_all_job_postings()
    userCandidateId = insert_candidate(userName, userEmail, userLocation, parsed_text, 1, userMotivation, userHobbies, userChallanges)
    motivation_keywords = extract_native_keywords(userMotivation, 20) 
    hobby_keywords = extract_native_keywords(userHobbies, 20) 
    challenges_keywords = extract_native_keywords(userChallanges, 20)
    resume_keywords = extract_native_keywords(parsed_text, 100) 
    all_keywords = [*motivation_keywords, *hobby_keywords, *challenges_keywords, *resume_keywords]
    # insert_candidate_keywords(userCandidateId, keywords, 0)
    print(all_keywords)
    result_string = ' '.join(all_keywords)
    similar_keywords = {}
    for job in jobs:
        similar_keywords[job] = compute_similar_keywords(result_string, jobs[job], 100)
    match = get_match(similar_keywords)
    job_match = get_job_application_by_id(match)
    title  = job_match[0]['title']
    application_link = job_match[0]['application_link']
    if job_match:
        st.title("Matched Jobs for You")
        st.header(f"{title} at {application_link}")
        # st.write(f"Candidate Match Score: ")



# def process_candidate(name, email, resume_file_path, max_features):
    # Existing code to extract keywords and insert candidate data
    # ...

    # Step 6: Match candidate to jobs
    # matches = match_candidate_to_jobs(candidate_id, candidate_keywords)

    # Step 7: Display matches to the candidate
    # for match in matches:
    #     print(f"Job Title: {match['title']}, Company: {match['company']}, Similarity: {match['similarity']}")


    # st.text_area('Cleaned Text', cleaned_text)

    # keywords = extract_keywords(cleaned_text, job_relevant_keywords)
    # st.write("Extracted Keywords: ", keywords)

    # st.header('Job Matches')

    # # Test jobs until we connect with database

    # matched_jobs = match_jobs(keywords, jobs, job_relevant_keywords)


    # for job, score in matched_jobs:
    #     st.write(f'Job: {job["title"]}, Match Score: {score}')

