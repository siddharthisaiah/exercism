def raindrops(number):
    factors = get_factors(number)
    raindrops = [(3,"Pling"), (5, "Plang"), (7, "Plong")]
    raindrop_speak = ""

    for raindrop in raindrops:
        if raindrop[0] in factors:
            raindrop_speak += raindrop[1]

    return str(number) if not raindrop_speak else raindrop_speak

def get_factors(n):
    # assumes n > 1
    facs = {1,n}

    for x in range(2, (n // 2) + 1):
        if n % x == 0:
            facs.add(x)
            
    return facs
