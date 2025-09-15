class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

class AVL_Tree(object):
    def __init__(self):
        # set True during an insertion if any rotation occurs
        self._rebalanced_this_insert = False

    # utility helpers
    def _height(self, node):
        return 0 if node is None else node.height

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        return node.height

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    # rotations
    def _right_rotate(self, y):
        self._rebalanced_this_insert = True
        x = y.left
        T2 = x.right
        # rotate
        x.right = y
        y.left = T2
        # update heights
        self._update_height(y)
        self._update_height(x)
        return x

    def _left_rotate(self, x):
        self._rebalanced_this_insert = True
        y = x.right
        T2 = y.left
        # rotate
        y.left = x
        x.right = T2
        # update heights
        self._update_height(x)
        self._update_height(y)
        return y

    # insert key (as int), return new root
    def insert(self, root, key):
        # convert incoming key (string from input) to int for numeric ordering
        k = int(key)

        # reset flag for this one insertion
        self._rebalanced_this_insert = False

        root = self._insert_rec(root, k)

        if self._rebalanced_this_insert:
            print("Not Balance, Rebalance!")
        return root

    def _insert_rec(self, node, key):
        # normal BST insert
        if node is None:
            return TreeNode(key)

        if key < node.val:
            node.left = self._insert_rec(node.left, key)
        else:
            # send duplicates to the right as a consistent policy
            node.right = self._insert_rec(node.right, key)

        # update height
        self._update_height(node)

        # rebalance
        bf = self._balance_factor(node)

        # LL case
        if bf > 1 and key < node.left.val:
            return self._right_rotate(node)

        # LR case
        if bf > 1 and key > node.left.val:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # RR case
        if bf < -1 and key > node.right.val:
            return self._left_rotate(node)

        # RL case
        if bf < -1 and key < node.right.val:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


# driver
myTree = AVL_Tree()
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")
