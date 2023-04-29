class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.ab = []

    def createNode(self, data):
        if self.root is None:
            n = Node(data)
            self.root = n
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def print_tree(self, node, traversal):
        if node is not None:
            traversal += (str(node.data) + "-")
            traversal = self.print_tree(node.left, traversal)
            traversal = self.print_tree(node.right, traversal)
        return traversal

    def levelOrder(self, root):
        q = []
        q.append(root)
        print(q)
        while len(q) != 0:
            root = q.pop(0)
            print(root.data, end=' ')
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)


tree = BinaryTree()
tree.createNode(1)
n = tree.root
tree.insert(n, 2)
tree.insert(n, 5)
tree.insert(n, 3)
tree.insert(n, 6)
tree.insert(n, 4)
# tree.insert(n, 30)
# tree.insert(n, 6)
# tree.insert(n, 8)
tree.levelOrder(n)
print("\n", tree.print_tree(n, ""))
