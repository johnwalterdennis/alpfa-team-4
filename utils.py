import re

import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer



def pre_process(text):
    text = text.lower()

    text = re.sub("","",text)

    text = re.sub("(\\d|\\W)+", " ", text)

    return text

# def parse_resume(filepath):
#     with open(filepath, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ""
#         for page_num in range(len(reader.pages)):
#             text += reader.pages[page_num].extract_text()
#         return text

# Use TF-IDF to retrieve keywords from user resume
# def extract_keywords(resume_text, job_relevant_keywords):
#     TFIDF = TfidfVectorizer(stop_words='english', max_features=10)
#     keywords = TFIDF.fit_transform([resume_text])
#     return TFIDF.get_feature_names_out()

# Can change the max_features to fit our testing desire
# def extract_keywords(resume_text, job_relevant_keywords):
#     tfidf = TfidfVectorizer(stop_words='english', max_features=100)

#     response = tfidf.fit_transform([resume_text])
#     tfidf_features = tfidf.get_feature_names_out()

#     tfidf_scores = response.toarray()[0]

#     tfidf_dict = {word: score for word, score in zip(tfidf_features, tfidf_scores)}

#     relevant_terms = {word: tfidf_dict[word] for word in tfidf_dict if word in job_relevant_keywords}

#     sorted_relevant_terms = sorted(relevant_terms.items(), key=lambda x: x[1], reverse=True)

#     top_relevant_keywords = [term[0] for term in sorted_relevant_terms]
#     return top_relevant_keywords

# Match keywords from resume to the jobs that the sponsors would like
# def match_jobs(user_keywords, jobs, job_relevant_keywords):
#     matches = []
#     for job in jobs:
#         job_keywords = extract_keywords(job['description'], job_relevant_keywords)
#         match_score = len(set(user_keywords).intersection(job_keywords))
#         if match_score > 0:
#             matches.append((job, match_score))

#     matches.sort(key=lambda x: x[1], reverse=True)
#     return matches