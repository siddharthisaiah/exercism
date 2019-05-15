import re

def abbreviate(words):
    """ 
    Join all the first letters of each word after splitting the string 'words' with
    the following delimters:[\s, -, _] and filtering out the empty strings. Convert
    the abbreviation to uppercase
    """
    return ''.join(word[0].upper() for word in re.split(r'[\s{1,}\-\_]', words) if word)
