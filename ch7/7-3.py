class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        return self.root

    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(' '+'     ' * level + str(node))
            self.printTree(node.left, level + 1)

    def countLessThanOrEqual(self, node, k):
        if node is None:
            return 0
        if node.data <= k:
            return 1 + self.countLessThanOrEqual(node.left, k) + self.countLessThanOrEqual(node.right, k)
        else:
            return self.countLessThanOrEqual(node.left, k)

# Main part
raw_input = input('Enter Input : ')
numbers_part, k_part = raw_input.split('/')
inp = [int(i) for i in numbers_part.strip().split()]
k = int(k_part.strip())

T = BST()
for i in inp:
    root = T.insert(i)

T.printTree(root)
print("--------------------------------------------------")
print(T.countLessThanOrEqual(root, k))
