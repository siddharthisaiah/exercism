def largest_product(series, size):

    if not series and size == 0: return 1

    if size == 0: return 1
    chunks = chunkify(series, size)


    try:
        chunks = list(map(string_product, chunks))
        
    except:
        raise ValueError("Invalid input data")

    
    return max(chunks)


def chunkify(l, s):
    chunked_list = [l[index:index+s] for index, value in enumerate(l)]
    return list(filter(lambda x: len(x) == s, chunked_list))


def string_product(s):
    if (int(s) == 0) or "0" in s: return 0
    s = int(s)
    result = 1
    while s != 0:
        result = result * (s % 10)
        s = s // 10
    return result



        
