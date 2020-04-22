import random
import math
from typing import List, Dict


def calc_tree_height(_len: int) -> int:
    return math.floor(math.log2(_len)) + 1


def get_middle_number(arr: List[int], start: int, end: int) -> int:
    num_pos = math.floor(end - start / 2.0)

    return arr[num_pos], num_pos


def build_tree(arr: List[int]) -> Dict:
    n = len(arr)
    if n == 1:
        return {
            "value": arr[0],
            "left": None,
            "right": None
        }
    elif n == 0:
        return None

    num_pos = math.floor(n / 2.0)

    return {
        "value": arr[num_pos],
        "left": build_tree(arr[:num_pos]),
        "right": build_tree(arr[num_pos + 1:])
    }


def mininal_tree() -> Dict:
    numbers = [n for n in random.sample(range(30), 9)]
    numbers.sort()

    print(numbers)

    # print(calc_tree_height(len(numbers)))

    return build_tree(numbers)
