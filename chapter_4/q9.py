from typing import List


def generate_permutation(a1: List[int],
                         a2: List[int],
                         prefix: List[int]) -> List[List[int]]:
    if len(a1) == 0:
        return [prefix + a2]

    lists = []

    for i in range(len(a2) + 1):
        if i == 0 and len(prefix) > 0:
            continue

        lists.append(prefix + a2[:i] + a1 + a2[i:])
        if len(a1) > 1:
            for j in range(len(a1) - 1):
                a1_new = a1[j + 1:]
                a2_new = a2[i:]
                prefix_new = prefix + a2[:i] + a1[:j + 1]
                lists += generate_permutation(a1=a1_new,
                                              a2=a2_new,
                                              prefix=prefix_new)

    return lists


def all_permutations(a1: List[int], a2: List[int]) -> List[List[int]]:
    return generate_permutation(a1=a1, a2=a2, prefix=[])
