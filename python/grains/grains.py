def on_square(square_number):
    if square_number < 1:
        raise ValueError("Square number cannot be less than 1")

    if square_number > 64:
        raise ValueError("Invalid square number")
    
    return pow(2, square_number - 1)


def total_after(square_number):
    if square_number < 1:
        raise ValueError("Square number cannot be less than 1")

    if square_number > 64:
        raise ValueError("Invalid square number")

    return sum(on_square(i) for i in range(1, square_number + 1))

