# Bob
# Bob is a lackadaisical teenager. In conversation, his responses are very limited.
# Bob answers 'Sure.' if you ask him a question.
# He answers 'Whoa, chill out!' if you yell at him.
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
# He says 'Fine. Be that way!' if you address him without actually saying
# anything.
# He answers 'Whatever.' to anything else.

import string
import re

def hey(phrase):

    phrase = phrase.replace('\n', ' ')
    phrase = phrase.strip()

    
    
    if phrase == "":
        return "Fine. Be that way!"
    
    # test for yelling questions
    if phrase[-1] == '?' and phrase == phrase.upper() and contains_letters(phrase):
        return "Calm down, I know what I'm doing!"

    # test for questions
    if phrase[-1] == '?':
        return "Sure."
    
    # test for yelling
    if phrase == phrase.upper() and contains_letters(phrase):
        return "Whoa, chill out!"

    return "Whatever."


def contains_letters(phrase):
    return re.search('\w[a-zA-Z]+', phrase)

