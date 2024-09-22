def find_intersection(list1, list2):
    keywords1 = set(list1)
    keywords2 = set(list2)

    intersection = keywords1.intersection(keywords2)
    return intersection