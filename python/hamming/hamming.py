def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Length of strands do not match!")

    hamming_distance = sum(1 for a, b in zip(strand_a, strand_b) if a != b)

    return hamming_distance
    
