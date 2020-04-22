from typing import List


def print_matrix(m: List[List[int]]):
    for r in range(len(m)):
        for c in range(len(m[0])):
            print(m[r][c], end="\t"),

        print()
