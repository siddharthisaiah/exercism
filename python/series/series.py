def slices(series, length):
    if len(series) == 0:
        raise ValueError("Series cannot be empty")
    if length <= 0:
        raise ValueError("Length cannot be less than 0")
    if length > len(series):
        raise ValueError("Length cannot be greater than the length of the series")
    
    return [series[ch:ch+length] for ch in range(len(series) - (length - 1))]

        
