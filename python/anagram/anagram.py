ANAGRAM = lambda sorted_word, candidate: sorted(candidate.lower()) == sorted_word

def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())
    return [c for c in candidates if c.lower() != word.lower() and ANAGRAM(sorted_word, c)]
    
