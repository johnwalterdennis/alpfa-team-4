import streamlit as st
import pandas as pd
import random

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
    job_id = st.text_input("Enter Job D")

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

if __name__ == "__main__":
    hr_candidate_viewer()