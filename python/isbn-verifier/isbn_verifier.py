def verify(isbn):
    
    legal_char = '0123456789X'

    if not(len(isbn) == 10 or len(isbn) == 13):
        return False

    isbn = isbn.upper().replace('-', '')
    isbn = list(isbn)
    
    if isbn[9] not in legal_char:
        return False
    
    for char in isbn[:9]:
        if char not in legal_char[:10]:
            return False
        
    if isbn[9] == 'X':
        isbn[9] = '10'
    
    isbn = list(map(int, isbn))
    isbn.reverse()
    
    prod = 0
    for n in range(10, 0, -1):
        prod = prod + (n * isbn[n-1])

    return prod % 11 == 0

