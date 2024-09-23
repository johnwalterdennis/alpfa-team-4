import streamlit as st
from database import insert_sponsor, insert_jobs
from keyword_extraction import extract_native_keywords
import itertools
import pandas as pd
import random


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


if 'registered' not in st.session_state:
    st.session_state['registered'] = False

# After registration

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

# Sample data for demonstration
def generate_sample_data():
    candidates = [
        {"name": f"Candidate {i}", 
         "email": f"candidate{i}@example.com", 
         "contact": f"+1 555-{random.randint(1000, 9999)}", 
         "experience": random.randint(1, 15),
         "match_percentage": random.randint(60, 100)} 
        for i in range(1, 21)
    ]
    return pd.DataFrame(candidates)

def hr_candidate_viewer():
    st.title("HR Candidate Viewer")

    # Job ID input
    job_id = st.text_input("Enter Job ID")

    if job_id:
        st.subheader(f"Potential Candidates for Job ID: {job_id}")

        # Generate sample data
        df = generate_sample_data()

        # Display candidates in a table
        st.dataframe(df)

        # Candidate details viewer
        st.subheader("Candidate Details")
        selected_candidate = st.selectbox("Select a candidate to view details", df['name'])

        if selected_candidate:
            candidate = df[df['name'] == selected_candidate].iloc[0]
            st.write(f"**Name:** {candidate['name']}")
            st.write(f"**Email:** {candidate['email']}")
            st.write(f"**Contact:** {candidate['contact']}")
            st.write(f"**Years of Experience:** {candidate['experience']}")
            st.write(f"**Job Match Percentage:** {candidate['match_percentage']}%")

            # Visual representation of job match percentage
            st.progress(candidate['match_percentage'] / 100)

    
if st.session_state['registered']:
    job_posting()
    hr_candidate_viewer()
else:
    sponsor_registration()