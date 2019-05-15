def square_of_sum(count):
    the_sum = sum(i for i in range(1, count+1))
    return pow(the_sum, 2)


def sum_of_squares(count):
     result = sum(pow(i, 2) for i in range(1, count+1))
     return result


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
