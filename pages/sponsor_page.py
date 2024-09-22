import streamlit as st
from database import insert_sponsor, insert_jobs
from keyword_extraction import extract_native_keywords
import itertools


def sponsor_registration():
    st.title("Sponsor Portal")
    with st.form("sponsor_registration"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        bio = st.text_input("bio")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Register")

    if submit:
            sponsor_id = insert_sponsor(name, email, bio, '', password)
            # print(sponsor_id)
            if sponsor_id:
                st.success("Registration successful!")
                # Navigate to Job Posting page
                st.session_state['sponsor_id'] = sponsor_id
                # Navigate to the Job Posting page
                st.write("Redirecting to Job Posting page...")
                st.session_state['registered'] = True
                # st.rerun
                job_posting()
            else:
                st.error("Registration failed.")
    else:
        st.error("Sponsor ID not found. Please register first.")
        st.session_state['registered'] = False

def job_posting():
    st.title("Post a job")
    sponsor_id = st.session_state.get("sponsor_id")

    if sponsor_id:
        st.write(f"Welcome Sponsor!")
        with st.form("Job posting form"):
            title = st.text_input("Job Title")
            description = st.text_area("what is the job description")
            personality = st.text_area("What kind of personality do you want for this role")
            application_link = st.text_area("Application link")
            submit_job = st.form_submit_button("Post Job")

        if submit_job:
            keyword_list1 = extract_native_keywords(description, 20)
            keyword_list2 = extract_native_keywords(personality, 20)
            keywords = [*keyword_list1, *keyword_list2]
            print(keywords)
            job_posting_id = insert_jobs(title, description, sponsor_id, keywords, personality, application_link)
            if job_posting_id:
                st.success("Job posting created successfully!")
                
            else:
                st.error("Failed to create job posting.")

    else:
        st.error("You need to register or log in as a sponsor first .")
        st.write("Please go to the Sponsor Registration page.")
        st.markdown("[Go to Sponsor Registration Page](/Sponsor_Registration)")
if 'registered' not in st.session_state:
    st.session_state['registered'] = False
    
if st.session_state['registered']:
    job_posting()
else:
    sponsor_registration()