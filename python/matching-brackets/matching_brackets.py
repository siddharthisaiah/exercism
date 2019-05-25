open_brackets = "{(["
close_brackets = "})]"
match_open_bracket = dict(zip(close_brackets, open_brackets))

def is_paired(input_string):
    stack = []

    for char in input_string:
        if char in open_brackets:
            stack.append(char)

        if char in close_brackets:
            if not stack or stack[-1] != match_open_bracket[char]:
                return False
            stack.pop()
                
    return not stack


