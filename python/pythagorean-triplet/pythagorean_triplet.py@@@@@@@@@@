import math

def triplets_with_sum(sum_of_triplet):
    triplets = []
    
    for a in range(2, int(sum_of_triplet / 3) + 1):
        for b in range(a+1, int(sum_of_triplet/2)+1):
            
            c = sum_of_triplet - a - b
            
            if pow(a,2) + pow(b,2)  == pow(c, 2):
                triplets.append((a, b, int(c)))

    return set(triplets)
