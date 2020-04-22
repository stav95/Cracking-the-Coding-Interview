# ord & chr
def is_unique(s: str) -> bool:
    if len(s) > 128:
        return False

    arr = [False] * 128
    for c in s:
        value = ord(c)

        if arr[value]:
            return False
        else:
            arr[value] = True

    return True


def is_unique_no_ds(s: str) -> bool:
    if len(s) > 128:
        return False

    for c in s:
        counter = 0
        for c2 in s:
            if c == c2:
                counter += 1
            if counter == 2:
                return False

    return True
