def is_armstrong(number):
    nums = [int(n) for n in str(number)]
    return sum(map(lambda x: x ** len(nums), nums)) == number
