# Get the name and surname frpm Users for calculating Jaccard Distance and Similarity
set_one = set(input('Please write your Name: '))
set_two = set(input('Please write your Surname: '))

def jaccard_similarity(set_one, set_two):
    # Find the intersection of two sets called nominator
    nominator = set_one.intersection(set_two)
    # Find the union of two sets called denominator
    denominator = set_one.union(set_two)
    # Calculate the Jaccard Similariry 
    similarity = len(nominator) / len(denominator)

    return similarity

def jaccard_distance(set_one, set_two):
    # Find the difference between two sets called nominator
    nominator = set_one.symmetric_difference(set_two)
    # Find the union of two sets called donominator
    denominator = set_one.union(set_two)
    # Calculate jaccard distance
    distance = len(nominator) / len(denominator)

    return distance

# Defining similarity and distance value on functions
sim = jaccard_similarity(set_one, set_two)

dis = jaccard_distance(set_one, set_two)

# Printing Values of these Similarity and Distance with Float
print(f"Jaccard Similarty result between your name and surname is {sim:.2f} \n")

print(f"Jaccard distance result between your name and surname is {dis:.2f}")