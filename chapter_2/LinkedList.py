from typing import List


class Node:
    def __init__(self, value: int, prev=None, _next=None):
        self.value = value
        self.prev = prev
        self.next = _next


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.tail = head
        self.count = 0 if head is None else 1

    def add_node(self, value: int) -> Node:
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.count = 1
        else:
            node = Node(value, self.tail)

            self.tail.next = node
            self.tail = node
            self.count += 1

        return self.tail

    def add_nodes(self, values: List[int]) -> Node:
        last = None
        for v in values:
            last = self.add_node(v)

        return last

    def remove_node(self, index: int) -> bool:
        idx = 0
        n = self.head

        while idx != index:
            if n.next is None:
                return False

            n = n.next
            idx += 1

        n.prev.next = n.next

        return True

    def print_list(self):
        n = self.head

        while n is not None:
            if n.next is not None:
                print(n.value, end=" --> ")
            else:
                print(n.value)

            n = n.next
