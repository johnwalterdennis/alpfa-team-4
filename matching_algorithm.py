from database import get_all_job_postings


# def match_candidate_to_jobs(candidate_id, similar_keywords):
#     # Retrieve all job postings
#     for job in similar_keywords:
#         job_keywords = job['required_keywords'].split(',')
#         similarity = compute_similarity(candidate_keywords, job_keywords)
#         if similarity >= threshold:
#             matches.append({
#                 'job_id': job['id'],
#                 'title': job['title'],
#                 'company': job['company'],
#                 'similarity': similarity
#             })
#     # Sort matches by similarity
#     matches.sort(key=lambda x: x['similarity'], reverse=True)
#     return matches

def get_match(job_dict):
    # Sort by length of the list of tuples (number of keywords) and then by the sum of weights
    sorted_jobs = sorted(
        job_dict.items(),
        key=lambda item: (len(item[1]), sum(weight for _, weight in item[1])),
        reverse=True
    )
    
    # Return the job ID with the most tuples and the highest combined weight
    return sorted_jobs[0][0] 