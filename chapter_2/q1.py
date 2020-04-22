from chapter_2.LinkedList import LinkedList


def remove_dups(ll: LinkedList):
    node = ll.head

    while node is not None:
        runner = node.next
        while runner is not None:
            if node.value == runner.value:
                runner.prev.next = runner.next

                if runner.next is not None:
                    runner.next.prev = runner.prev

            runner = runner.next

        node = node.next
