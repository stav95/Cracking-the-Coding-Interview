from typing import List


def rotate_matrix(m: List[List[int]]) -> List[List[int]]:
    n = len(m)
    k = n - 1

    new_m = []
    for i in range(n):
        new_row = []
        for j in range(n):
            new_row.append(m[k - j][i])

        new_m.append(new_row)

    return new_m


def rotate_matrix_in_place(m: List[List[int]]):
    n = len(m)
    k = n - 1
    layers = int(n / 2)

    for i in range(layers):
        for j in range(n - 1 - (i * 2)):
            top_left = m[i][j + i]
            top_right = m[j + i][k - i]
            bottom_right = m[k - i][k - j - i]
            bottom_left = m[k - j - i][i]

            m[i][j + i] = bottom_left
            m[j + i][k - i] = top_left
            m[k - i][k - j - i] = top_right
            m[k - j - i][i] = bottom_right
