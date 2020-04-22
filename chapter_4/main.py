import networkx as nx


def generate_random_graph() -> nx.Graph:
    return nx.fast_gnp_random_graph(10, 0.2)


# from chapter_4.q2 import mininal_tree
#
# mininal_tree()


# from chapter_4.q3 import list_of_depths

# print(list_of_depths())


from chapter_4.q9 import all_permutations

a1 = [1, 2, 3]
a2 = [4, 5, 3]

print(all_permutations(a1, a2))
print(len(all_permutations(a1, a2)))
