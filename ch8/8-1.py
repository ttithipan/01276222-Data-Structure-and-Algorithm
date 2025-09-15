class AVLTree:

    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root=None):
        self.root = None if root is None else root

    # ---- public insert ----
    def add(self, data):
        # convert to int for correct numeric ordering (negatives, multi-digits)
        val = int(data)
        self.root = AVLTree._add(self.root, val)

    # ---- internal insert with rebalancing ----
    def _add(root, data):
        if root is None:
            return AVLTree.AVLNode(data)

        # BST insert: duplicates go to the right subtree (to match expected outputs)
        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)

        # update height
        root.setHeight()

        # rebalance
        balance = root.balanceValue()

        # right heavy
        if balance > 1:
            # RR case
            if root.right.balanceValue() >= 0:
                return AVLTree.rotateLeftChild(root)
            # RL case
            else:
                root.right = AVLTree.rotateRightChild(root.right)
                return AVLTree.rotateLeftChild(root)

        # left heavy
        if balance < -1:
            # LL case
            if root.left.balanceValue() <= 0:
                return AVLTree.rotateRightChild(root)
            # LR case
            else:
                root.left = AVLTree.rotateLeftChild(root.left)
                return AVLTree.rotateRightChild(root)

        return root

    # ---- rotations ----
    def rotateLeftChild(root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        # update heights bottom-up
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    # ---- post-order traversal ----
    def postOrder(self):
        vals = []
        AVLTree._postOrder(self.root, vals)
        # format exactly like the samples (space after each value, blank allowed)
        print("AVLTree post-order : " + (" ".join(map(str, vals)) + " " if vals else ""))

    def _postOrder(root, out_list):
        if root is None:
            return
        AVLTree._postOrder(root.left, out_list)
        AVLTree._postOrder(root.right, out_list)
        out_list.append(root.data)

    # ---- pretty tree printer (given) ----
    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node, level=0):
        if node is not None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)


# ---------- driver ----------
avl1 = AVLTree()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()
