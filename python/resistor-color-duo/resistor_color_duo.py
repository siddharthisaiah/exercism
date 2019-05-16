color_codes = [
            'black',
            'brown',
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'violet',
            'grey',
            'white'
        ]

def value(colors):
    str_val = ''

    for color in colors:
        str_val += str(color_codes.index(color))

    return int(str_val)
