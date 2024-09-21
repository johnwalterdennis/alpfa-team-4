import re
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer

def pre_process(text):
    text = text.lower()

    text = re.sub("","",text)

    text = re.sub(r"[^\w\s+#]"," ", text)

    return text

def parse_resume(filepath):
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text


# Can change the max_features to fit our testing desire
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

def extract_keywords(resume_text, job_relevant_keywords):
    # Ensure job_relevant_keywords are unique
    job_relevant_keywords = list(set(job_relevant_keywords))

    # Pre-process the resume text
    resume_text = pre_process(resume_text)

    # Use TfidfVectorizer to extract keywords, with vocabulary set to job-relevant keywords
    vectorizer = TfidfVectorizer(vocabulary=job_relevant_keywords, token_pattern=r'\b\w[\w+#]+\b')

    # Fit and transform the resume text
    tfidf_matrix = vectorizer.fit_transform([resume_text])

    # Extract the tf-idf scores
    tfidf_scores = tfidf_matrix.toarray().flatten()

    # Map the keywords to their tf-idf scores
    keyword_scores = dict(zip(vectorizer.get_feature_names_out(), tfidf_scores))

    # Filter the keywords to only include those with non-zero scores
    non_zero_keywords = {keyword: score for keyword, score in keyword_scores.items() if score > 0}

    # Sort the keywords by score in descending order
    sorted_non_zero_keywords = sorted(non_zero_keywords.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted keywords with scores
    # This returns a Tuple
    return sorted_non_zero_keywords

# Match keywords from resume to the jobs that the sponsors would like
def match_jobs(user_keywords, job_skills, max_size, job_relevant_keywords):
    user_keywords_list = []
    job_keywords_list = []
    job_skills_string = ' '.join(job_skills)
    job_keywords_tuple = extract_keywords(job_skills_string, job_relevant_keywords)

    for id, element in enumerate(job_keywords_tuple):
        job_keywords_list.append(element[0])
        if len(user_keywords_list) >= max_size:
            break

    for id, element in enumerate(user_keywords):
        print(id)
        print(element)
        user_keywords_list.append(element[0])
        if len(user_keywords_list) >= max_size:
            break


    match_score = find_intersection(user_keywords_list, job_keywords_list)

    # matches.sort(key=lambda x: x[1], reverse=True)
    return match_score

def find_intersection(list1, list2):
    keywords1 = set(list1)
    keywords2 = set(list2)

    intersection = keywords1.intersection(keywords2)

    return intersection
