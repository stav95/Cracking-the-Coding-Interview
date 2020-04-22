from typing import List
from copy import deepcopy


def zero_row(m: List[List[int]], row: int):
    for c in range(len(m[0])):
        m[row][c] = 0


def zero_col(m: List[List[int]], col: int):
    for r in range(len(m)):
        m[r][col] = 0


def zero_matrix(m: List[List[int]]) -> List[List[int]]:
    m_cloned = deepcopy(m)

    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 0:
                zero_row(m_cloned, r)
                zero_col(m_cloned, c)

    return m_cloned
