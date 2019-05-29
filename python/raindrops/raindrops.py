def raindrops(number):
    raindrops = [(3,"Pling"), (5, "Plang"), (7, "Plong")]
    raindrop_speak = [raindrop[1] for raindrop in raindrops if number % raindrop[0] == 0]
    
    return str(number) if not raindrop_speak else "".join(raindrop_speak)
