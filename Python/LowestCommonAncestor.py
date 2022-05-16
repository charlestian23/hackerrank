class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root, v1, v2):
    if root is None:
        return root
    if root.info == v1 or root.info == v2:
        return root
    v1_next_node = None
    v2_next_node = None
    if v1 > root.info:
        v1_next_node = root.right
    else:
        v1_next_node = root.left
    if v2 > root.info:
        v2_next_node = root.right
    else:
        v2_next_node = root.left
    if v1_next_node != v2_next_node:
        return root
    return lca(v1_next_node, v1, v2)


tree = BinarySearchTree()
t = 25
first_string_input = "23 16 15 9 6 17 10 13 8 26 18 2 22 24 12 5 20 25 21 4 19 1 3 14 7"
arr = list(map(int, first_string_input.split()))
for i in range(t):
    tree.create(arr[i])
second_string_input = "23 3"
v = list(map(int, second_string_input.split()))
ans = lca(tree.root, v[0], v[1])
print(ans.info)
