def is_palindrome_permutation(s: str) -> str:
    d = {}

    for c in s:
        d.update({
            c: d.get(c, 0) + 1
        })

    odds = 0
    for v in d.values():
        if v % 2 != 0:
            odds += 1
            if odds > 1:
                return False

    return True