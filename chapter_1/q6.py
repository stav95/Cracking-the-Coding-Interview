def string_compression(s: str) -> str:
    new_string = ""

    c = s[0]
    counter = 0
    for i in range(len(s)):
        if c == s[i]:
            counter += 1
        else:
            new_string += f'{c}{counter}'
            counter = 1
            c = s[i]

    new_string += f'{c}{counter}'

    if len(s) > len(new_string):
        return new_string
    else:
        return s
