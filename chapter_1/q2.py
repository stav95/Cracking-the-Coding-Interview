import numpy as np


def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    arr1 = [c for c in s1]
    arr1.sort()

    arr2 = [c for c in s2]
    arr2.sort()

    return np.array_equal(arr1, arr2)
