def find_anagrams(word, candidates):
    sorted_word = ''.join(sorted(word.lower()))
    return list(filter(lambda cand: cand.lower() != word.lower() and is_anagram(sorted_word, cand), candidates))


def is_anagram(sorted_word, candidate):
    sorted_candidate = ''.join(sorted(candidate.lower()))
    return sorted_candidate == sorted_word
    
    
