from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(text, max_features=20):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=max_features)
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_array = vectorizer.get_feature_names_out()
    return feature_array

def extract_keywords(resume_text, job_relevant_keywords):
    tfidf = TfidfVectorizer(stop_words='english', max_features=100)

    response = tfidf.fit_transform([resume_text])
    tfidf_features = tfidf.get_feature_names_out()

    tfidf_scores = response.toarray()[0]

    tfidf_dict = {word: score for word, score in zip(tfidf_features, tfidf_scores)}

    relevant_terms = {word: tfidf_dict[word] for word in tfidf_dict if word in job_relevant_keywords}

    sorted_relevant_terms = sorted(relevant_terms.items(), key=lambda x: x[1], reverse=True)

    top_relevant_keywords = [term[0] for term in sorted_relevant_terms]
    return top_relevant_keywords