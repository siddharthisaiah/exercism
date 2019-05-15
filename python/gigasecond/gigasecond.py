import datetime

def add_gigasecond(birth_date):
    '''
    Calculate the moment when someone has lived for 10^9 seconds.
    A gigasecond is 10^9 (1,000,000,000) seconds.
    '''

    gigasecond = 1000000000
    end_date = birth_date + datetime.timedelta(seconds=gigasecond)

    return end_date
