def urlify(s: str) -> str:
    s = s.strip()

    new_arr = []
    for c in s:
        if c != ' ':
            new_arr.append(c)
        else:
            if new_arr[-1] != "%20":
                new_arr.append("%20")

    return ''.join(new_arr)
