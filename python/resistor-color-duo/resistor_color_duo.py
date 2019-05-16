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
    colors = list(reversed(colors))
    result = 0
    
    for index, val in enumerate(colors):
        result += color_codes.index(val) * pow(10, index)

    return result
