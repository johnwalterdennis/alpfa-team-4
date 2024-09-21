def match_jobs(user_keywords, jobs, job_relevant_keywords):
    matches = []
    for job in jobs:
        job_keywords = extract_keywords(job['description'], job_relevant_keywords)
        match_score = len(set(user_keywords).intersection(job_keywords))
        if match_score > 0:
            matches.append((job, match_score))

    matches.sort(key=lambda x: x[1], reverse=True)
    return matches