from sklearn.feature_extraction.text import TfidfVectorizer

def extract_native_keywords(text, max_features=50):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=max_features)
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_array = vectorizer.get_feature_names_out()
    return feature_array


def compute_similar_keywords(text, job_relevant_keywords, max_features):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=max_features) #this initialized the vectorizer to ignore stop words in english like "is", "like"
    #it also sets the max_features(keywords) as the number passed in at the method call
    response = vectorizer.fit_transform([text]) #this is when the vectorizer reads the text, it is read in as a list[] because the method expect a bunch of pages
    tfidf_features = vectorizer.get_feature_names_out() #this returns the top keywords (keywords=features)

    tfidf_scores = response.toarray()[0] #the fit_transform method returns a matrix of scores for each page but we are only reading one page so we just need the top row of the array 

    tfidf_dict = {word:score for (word, score) in zip(tfidf_features, tfidf_scores)} #dict comprenshion, this line creates a dictionary for all (word and score)s that the zip function returns, the zip function returns a list of tuples [(a,b), (c,d)]
    # example myDict = { k:v for (k,v) in zip(keys, values)}  
    relevant_terms = {word:tfidf_dict[word] for word in tfidf_dict if word in job_relevant_keywords}#this method creates a dictionary for all (keys and tfidf[keys]) if the word is in the relevant keyword list

    sorted_relevant_terms = sorted(relevant_terms.items(), key=lambda x: x[1], reverse=True) #this line sorts the dictionary, relevant_terms.items() returns a list of tuples from the dictionary, the sort function then sorts it by the second value in each tuple "lambda x: x[1]" x is the tuple and x[1] is the second valuae int tuple, reverse makes the list descending since the default is ascending

    # top_relevant_keywords = [term[0] for term in sorted_relevant_terms]
    # return top_relevant_keywords
    return sorted_relevant_terms
