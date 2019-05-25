def is_paired(input_string):
    opening_bracket = "{(["
    closing_bracket = "})]"

    open_stack = []

    while input_string:
        first_char = input_string[0]

        if first_char in opening_bracket:
            open_stack.append(first_char)


        if first_char in closing_bracket:
            # check if open_stack is not empty
            if not open_stack: return False

            if bracket_matches(open_stack[-1], first_char):
                open_stack.pop()
            else:
                return False

        input_string = input_string[1:]


    return len(open_stack) == 0 and input_string == ""


def bracket_matches(opening_bracket, closing_bracket):
    closing_bracket_map = {
        '}' : '{',
        ')' : '(' ,
        ']' : '['
    }

    return closing_bracket_map[closing_bracket] == opening_bracket
