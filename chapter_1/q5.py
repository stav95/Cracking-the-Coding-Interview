def insert_or_remove_char(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return insert_or_remove_char(s2, s1)

    # s1 is shorter than s2.
    n = len(s1)
    for i in range(len(s2)):
        if n == i:
            s1 += s2[i]
        else:
            if s1[i] != s2[i]:
                s1 = s1[:i] + s2[i] + s1[i:]
                break

    return s1 == s2


def replace_char(s1: str, s2: str) -> bool:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            s1 = s1[:i] + s2[i] + s1[i + 1:]
            break

    return s1 == s2


def one_away(s1: str, s2: str) -> bool:
    if len(s1) == len(s2):
        if s1 == s2:
            return True
        else:
            return replace_char(s1, s2)
    elif abs(len(s1) - len(s2)) == 1:
        return insert_or_remove_char(s1, s2)

    return False
