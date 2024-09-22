from keyword_extraction import extract_keywords

# # Match keywords from resume to the jobs that the sponsors would like
# def match_jobs(user_keywords, job_skills, max_size, job_relevant_keywords):
#     user_keywords_list = []
#     job_keywords_list = []
#     job_skills_string = ' '.join(job_skills)
#     job_keywords_tuple = extract_keywords(job_skills_string, job_relevant_keywords, 100)
#
#     for id, element in enumerate(job_keywords_tuple):
#         job_keywords_list.append(element[0])
#         if len(user_keywords_list) >= max_size:
#             break
#
#     for id, element in enumerate(user_keywords):
#         print(id)
#         print(element)
#         user_keywords_list.append(element[0])
#         if len(user_keywords_list) >= max_size:
#             break
#
#
#     match_score = find_intersection(user_keywords_list, job_keywords_list)
#
#     # matches.sort(key=lambda x: x[1], reverse=True)
#     return match_score

def match_jobs(user_keywords, jobs_skills, max_size, job_relevant_keywords):
    # List to store job match scores
    job_match_scores = []

    # Convert user keywords into a list of the top keywords
    user_keywords_list = [element[0] for element in user_keywords[:max_size]]

    # Loop over each job and calculate the similarity score
    # THIS USES A DICT
    for job_name, job_skills in jobs_skills.items():
        # Create a string of job skills and extract keywords
        job_skills_string = ' '.join(job_skills)
        job_keywords_tuple = extract_keywords(job_skills_string, job_relevant_keywords, max_size)

        # Convert job keywords into a list
        job_keywords_list = [element[0] for element in job_keywords_tuple[:max_size]]

        # Calculate the match score (intersection over union) as a percentage
        match_score = find_similarity_score(user_keywords_list, job_keywords_list)

        # Store the job name and score as a tuple
        job_match_scores.append((job_name, f"{match_score * 100:.2f}%"))  # Convert to percentage

    # Sort the jobs by their match score in descending order
    # sorted_job_matches = sorted(job_match_scores, key=lambda x: x[1], reverse=True)
    sorted_job_matches = sorted(job_match_scores, key=lambda x: float(x[1].replace('%', '')), reverse=True)

    return sorted_job_matches


def find_similarity_score(user_keywords_list, job_keywords_list):
    # Convert lists to sets for easier comparison
    user_set = set(user_keywords_list)
    job_set = set(job_keywords_list)

    # Calculate the intersection and union of both sets
    intersection = user_set.intersection(job_set)
    union = user_set.union(job_set)

    # Using Jaccard similarity to find similarity score
    similarity_score = len(intersection) / len(union) if len(union) != 0 else 0

    return similarity_score