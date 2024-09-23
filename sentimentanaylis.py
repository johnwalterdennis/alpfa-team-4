import streamlit as st
import re

# Pre-defined soft skills and keywords related to them
soft_skills_keywords = {
    "Communication": ["communicate", "listen", "present", "articulate", "express"],
    "Teamwork": ["team", "collaborate", "cooperate", "assist", "together"],
    "Problem-solving": ["solve", "resolve", "analyze", "solution", "issue", "troubleshoot"],
    "Leadership": ["lead", "guide", "mentor", "direct", "influence"],
    "Adaptability": ["adapt", "change", "flexible", "shift", "adjust", "pivot"],
    "Time Management": ["deadline", "prioritize", "schedule", "manage time", "organize"],
    "Creativity": ["innovate", "create", "design", "idea", "imagine", "brainstorm"]
}

# Function to analyze soft skills based on answers
def analyze_soft_skills(answers):
    identified_skills = {}
    for skill, keywords in soft_skills_keywords.items():
        # Search for keywords in the candidate's answer text
        count = sum(len(re.findall(keyword, answers, re.IGNORECASE)) for keyword in keywords)
        if count > 0:
            identified_skills[skill] = count
    return identified_skills

# Input text area for HR to paste candidate's answers
candidate_answers = st.text_area("Enter the candidate's answers to the interview questions:")

if candidate_answers:
    # Analyze the soft skills in the answers
    skills = analyze_soft_skills(candidate_answers)
    
    if skills:
        st.write("### Soft Skills Identified:")
        for skill, count in skills.items():
            st.write(f"- {skill}: Mentioned {count} times")
    else:
        st.write("No soft skills identified from the given answers.")
else:
    st.write("Please input the candidate's answers to analyze soft skills.")
