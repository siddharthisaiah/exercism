def word_count(phrase):
    import string

    wc = dict()
    phrase = phrase.lower()

    for p in string.punctuation:
        if p != "'":            # do not split on '(apostrophe) or there will be problems with words like < don't >
            phrase = phrase.replace(p, ' ')

    try:
        for word in phrase.split():
            wc[word.strip("'")] = wc.get(word, 0) + 1  # strip leading and trailing apostrophes (') so 'large' == large
        return wc
    except:
        raise Exception("Somethings gone wrong")



# good example from exercism
#
# http://exercism.io/submissions/ab298c6279f34bec8de9e3623c01f6d1

# import string

# def word_count(phrase):
#     '''
#     Count the occurrences of each word in a string, return as a dictionary
#     '''
#     # replace all punctuation except apostrophes with whitespace
#     for p in string.punctuation:
#         if p != "'":
#             phrase = phrase.replace(p, ' ')

#     # convert string to list of words and strip enclosing quotation marks
#     word_list = [x.lower().strip("'") for x in phrase.split()]

#     # index and count words in list
#     return dict([(key, sum([1 for word in word_list if word == key])) for key in word_list])

