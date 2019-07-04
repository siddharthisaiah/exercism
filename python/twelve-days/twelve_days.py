def recite(start_verse, end_verse):
    verses = [0, 'first', 'second', 'third', 'fourth',
              'fifth', 'sixth', 'seventh', 'eighth',
              'ninth', 'tenth', 'eleventh', 'twelfth']

    gifts = ["twelve Drummers Drumming",
             "eleven Pipers Piping", 
             "ten Lords-a-Leaping",
             "nine Ladies Dancing",
             "eight Maids-a-Milking",
             "seven Swans-a-Swimming",
             "six Geese-a-Laying",
             "five Gold Rings",
             "four Calling Birds",
             "three French Hens",
             "two Turtle Doves",
             "and a Partridge in a Pear Tree"]
    
    song = []
    
    for v in range(start_verse, end_verse + 1):
        v_gifts = gifts[-v].replace('and ', '') if v == 1 else ', '.join(gifts[-v:]) # gifts dont include the word 'and ' if its the first verse
        song.append(f"On the {verses[v]} day of Christmas my true love gave to me: {v_gifts}.")
        
    return song
