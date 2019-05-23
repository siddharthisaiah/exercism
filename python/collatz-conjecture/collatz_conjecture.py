next_collatz = lambda n: n/2 if (n %2 == 0) else (3 * n) + 1

def collatz_steps(number):
    steps = 0

    if number <= 0:
        raise ValueError("Invalid input")
    
    while number != 1:
        steps, number = steps+1, next_collatz(number)

    return steps


