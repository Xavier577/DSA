import json


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dict_binary_tree(node: Node) -> dict:
    tree = {}
    """
    Tree
    {
    value
    left: { value, left: {...}, right: {...} }
    right: { value, left: {...}, right: {...} }
    }
    """

    if node == None:
        return tree

    tree['value'] = node.value

    if node.left != None:
        tree['left'] = dict_binary_tree(node.left)

    if node.right != None:
        tree['right'] = dict_binary_tree(node.right)

    return tree


class Tree:
    def __init__(self, root=None):
        self.root = root

    def search(self, value) -> bool:
        if self.root == None:
            return False

        current = self.root

        parent = None

        while current != None:
            parent = current

            if value == parent.value:
                return True

            if value < parent.value:
                current = current.left
                if current != None:
                    continue

            else:
                current = current.right
                if current != None:
                    continue
        else:
            return False

    def append(self, node: Node):
        if self.root == None:
            self.root = node
            return

        current = self.root

        while True:
            parent = current

            # go to left of the tree

            if node.value < parent.value:
                current = current.left

                if current == None:
                    parent.left = node
                    return
            # go to right of the tree
            else:
                current = current.right

                if current == None:
                    parent.right = node
                    return

    def __dict__(self):
        tree = {}

        if self.root == None:
            return tree

        tree["root"] = dict_binary_tree(self.root)

        return tree


tree = Tree()

tree.append(Node(19))
tree.append(Node(2))
tree.append(Node(5))
tree.append(Node(3))
tree.append(Node(6))
tree.append(Node(17))
tree.append(Node(4))
tree.append(Node(7))
print(json.dumps(tree.__dict__(), indent=4))

print(tree.search(1))
print(tree.search(2))
print(tree.search(3))
print(tree.search(4))
print(tree.search(5))
print(tree.search(6))
print(tree.search(7))

print("8 in Tree ?")
print(tree.search(8))

print(tree.__dict__())

# Binary Tree inline implementation

root_node = Node(1)
node_2 = Node(2)
node_3 = Node(3)

root_node.left = node_2
root_node.right = node_3

node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)

node_2.left = node_4
node_2.right = node_5

node_3.left = node_6
node_3.right = node_7

inline_tree = Tree(root_node)

print(json.dumps(inline_tree.__dict__(), indent=2))
