def sum_of_multiples(limit, factors):
    return sum({x for f in factors for x in range(f, limit, f)})


    

    
