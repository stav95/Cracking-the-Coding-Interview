from typing import List


def peek(s: List[int]) -> int:
    return s[len(s) - 1]


def pop_last(s: List[int]) -> int:
    return s.pop(len(s) - 1)


def push_last(s: List[int], value: int) -> int:
    s.insert(len(s), value)


def sort_stack(_list: List[int]) -> List[int]:
    if len(_list) == 0:
        return []

    s = [_list[0]]
    s_tmp = []

    for n in _list[1:]:
        while len(s) > 0 and peek(s) < n:
            push_last(s_tmp, pop_last(s))

        push_last(s, n)

        while len(s_tmp) > 0:
            push_last(s, pop_last(s_tmp))

    return s
