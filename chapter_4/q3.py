from chapter_4.q2 import mininal_tree
from typing import List, Dict


def pre_order_traversal(lists: List[List[int]],
                        node: Dict,
                        height: int):
    if "value" not in node:
        return None

    node_value = node["value"]
    if len(lists) >= height:
        lists[height - 1].append(node_value)
    else:
        lists.append([node_value])

    node_left = node["left"]
    if node_left is not None:
        pre_order_traversal(lists, node_left, height + 1)

    node_right = node["right"]
    if node_right is not None:
        pre_order_traversal(lists, node_right, height + 1)


def create_lists(tree: Dict) -> List[List[int]]:
    if "value" not in tree:
        return None

    lists = [[tree['value']]]

    node_left = tree["left"]
    if node_left is not None:
        pre_order_traversal(lists, node_left, 2)

    node_right = tree["right"]
    if node_right is not None:
        pre_order_traversal(lists, node_right, 2)

    return lists


def list_of_depths() -> List[List[int]]:
    lists = create_lists(mininal_tree())

    return lists
