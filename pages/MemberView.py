import os

import streamlit as st
from utils import pre_process
from parse_resume import parse_resume
from matching_algorithm import match_jobs
from keyword_extraction import extract_keywords

job_relevant_keywords = [
    "python", "machine learning", "data analysis", "flask", "django", "sql",
    "cloud", "api", "tensorflow", "numpy","java","c#", "c++", "c", "linux","mysql", "postgresql",
    "rust","javascript", "ruby", "go", "typescript", "php", "html" "css", "node", "js",
    "git", "github", "spring", "pandas", "nosql", "mongodb", "aws", "azure", "nlp", "kotlin",
    "swift", "golang", "figma", "unity", "pytorch", "docker", ""
]

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

        parsed_text = parse_resume(filename)
        cleaned_text = pre_process(parsed_text)

        st.text_area('Cleaned Text', cleaned_text)

        # Takes the resumes cleaned text and finds the top skills attached to it
        keywords = extract_keywords(cleaned_text, job_relevant_keywords, 1000)
        st.write("Extracted Keywords: ", keywords)

        st.header('Job Matches')
        # Test Skill list
        job_name = "Software Developer"
        jobs_skills = {
            'Backend Developer': ['python', 'java', 'c++', 'sql', 'c#', 'spring', 'node.js', 'docker', 'kubernetes',
                                  'graphql'],
            'Frontend Developer': ['javascript', 'html', 'css', 'react', 'vue', 'angular', 'sass', 'typescript',
                                   'webpack', 'npm'],
            'Data Scientist': ['python', 'machine learning', 'pandas', 'sql', 'tensorflow', 'scikit-learn', 'r',
                               'matplotlib', 'keras', 'deep learning'],
            'Morgan Stanley Developer': ['java', 'spring', 'mysql', 'postgresql', 'microservices', 'docker', 'kafka',
                                         'hibernate', 'rest api', 'aws'],
            'DevOps Engineer': ['linux', 'docker', 'kubernetes', 'aws', 'terraform', 'ansible', 'bash', 'jenkins',
                                'ci/cd', 'monitoring'],
            'Mobile App Developer': ['swift', 'kotlin', 'react native', 'flutter', 'android', 'ios', 'dart',
                                     'objective-c', 'firebase', 'graphql'],
            'UI/UX Designer': ['figma', 'adobe xd', 'sketch', 'wireframing', 'prototyping', 'user research',
                               'interaction design', 'usability testing', 'html', 'css'],
            'Cloud Engineer': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform', 'ansible', 'linux',
                               'networking', 'cloudformation'],
            'Cybersecurity Analyst': ['network security', 'firewalls', 'penetration testing', 'siem', 'ids', 'ips',
                                      'incident response', 'encryption', 'linux', 'ethical hacking'],
            'Machine Learning Engineer': ['python', 'tensorflow', 'pytorch', 'scikit-learn',
                                          'natural language processing', 'neural networks', 'data engineering', 'spark',
                                          'r', 'matplotlib'],
            'Full Stack Developer': ['javascript', 'node.js', 'react', 'python', 'java', 'sql', 'mongodb', 'docker',
                                     'graphql', 'rest api'],
            'Data Engineer': ['python', 'sql', 'spark', 'hadoop', 'etl', 'airflow', 'big data', 'aws', 'gcp',
                              'data warehousing'],
            'Game Developer': ['c++', 'unity', 'unreal engine', 'c#', 'game design', '3d modeling', 'animation', 'ai',
                               'vr/ar', 'shaders'],
            'Blockchain Developer': ['solidity', 'ethereum', 'hyperledger', 'cryptography', 'smart contracts', 'dapps',
                                     'web3', 'python', 'rust', 'consensus algorithms'],
            'Network Engineer': ['cisco', 'routing', 'switching', 'firewalls', 'tcp/ip', 'vpn', 'load balancing',
                                 'network security', 'dns', 'troubleshooting'],
            'IT Support Specialist': ['windows', 'linux', 'troubleshooting', 'active directory', 'networking',
                                      'customer service', 'hardware', 'software installation', 'ticketing systems',
                                      'remote support'],
            'Artificial Intelligence Engineer': ['python', 'tensorflow', 'pytorch', 'deep learning', 'computer vision',
                                                 'nlp', 'neural networks', 'machine learning', 'r',
                                                 'reinforcement learning'],
            'Systems Administrator': ['linux', 'windows server', 'bash', 'powershell', 'virtualization', 'vmware',
                                      'networking', 'active directory', 'backup', 'monitoring'],
            'Product Manager': ['project management', 'agile', 'scrum', 'jira', 'user stories', 'market research',
                                'roadmapping', 'analytics', 'communication', 'ux'],
            'Digital Marketer': ['seo', 'google analytics', 'content marketing', 'social media', 'ppc',
                                 'email marketing', 'copywriting', 'sem', 'adwords', 'facebook ads'],
            'Data Analyst': ['excel', 'sql', 'tableau', 'power bi', 'data visualization', 'python', 'r', 'statistics',
                             'data cleaning', 'dashboards']
        }

        # Returns the top list of skills that are matched from the job and resume
        matched_skills = match_jobs(keywords, jobs_skills, 10, job_relevant_keywords)
        st.write(list(dict.fromkeys(matched_skills)))


