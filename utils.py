import re
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer

# def pre_process(text):
#     text = text.lower()
#
#     text = re.sub("","",text)
#
#     text = re.sub(r"[^\w\s+#]"," ", text)
#
#     return text
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
# def extract_keywords(resume_text, job_relevant_keywords):
#     tfidf = TfidfVectorizer(stop_words='english', max_features=100)
#
#     response = tfidf.fit_transform([resume_text])
#     tfidf_features = tfidf.get_feature_names_out()
#
#     tfidf_scores = response.toarray()[0]
#
#     tfidf_dict = {word: score for word, score in zip(tfidf_features, tfidf_scores)}
#
#     relevant_terms = {word: tfidf_dict[word] for word in tfidf_dict if word in job_relevant_keywords}
#
#     sorted_relevant_terms = sorted(relevant_terms.items(), key=lambda x: x[1], reverse=True)
#
#     top_relevant_keywords = [term[0] for term in sorted_relevant_terms]
#     return top_relevant_keywords

# def extract_keywords(resume_text, job_relevant_keywords):
#     # Ensure job_relevant_keywords are unique
#     job_relevant_keywords = list(set(job_relevant_keywords))
#
#     # Pre-process the resume text
#     resume_text = pre_process(resume_text)
#
# #     response = tfidf.fit_transform([resume_text])
# #     tfidf_features = tfidf.get_feature_names_out()
#     # Use TfidfVectorizer to extract keywords, with vocabulary set to job-relevant keywords
#     vectorizer = TfidfVectorizer(vocabulary=job_relevant_keywords, token_pattern=r'\b\w[\w+#]+\b')
#
#     # Fit and transform the resume text
#     tfidf_matrix = vectorizer.fit_transform([resume_text])
#
#     # Extract the tf-idf scores
#     tfidf_scores = tfidf_matrix.toarray().flatten()
#
#     # Map the keywords to their tf-idf scores
#     keyword_scores = dict(zip(vectorizer.get_feature_names_out(), tfidf_scores))
#
#     # Filter the keywords to only include those with non-zero scores
#     non_zero_keywords = {keyword: score for keyword, score in keyword_scores.items() if score > 0}
#
#     # return top_relevant_keywords
#     # Sort the keywords by score in descending order
#     sorted_non_zero_keywords = sorted(non_zero_keywords.items(), key=lambda x: x[1], reverse=True)
#
#     # Return the sorted keywords with scores
#     # This returns a Tuple
#     return sorted_non_zero_keywords

