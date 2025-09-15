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
        self._rotation_msg = None  # set to a string when a rotation happens

    # ---- helpers ----
    def _h(self, n):
        return 0 if n is None else n.height

    def _upd(self, n):
        n.height = 1 + max(self._h(n.left), self._h(n.right))
        return n.height

    def _bf(self, n):
        return self._h(n.left) - self._h(n.right)

    # ---- rotations (set message exactly once per insertion) ----
    def _right_rotate(self, y, set_msg=None):
        if set_msg and self._rotation_msg is None:
            self._rotation_msg = set_msg
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._upd(y)
        self._upd(x)
        return x

    def _left_rotate(self, x, set_msg=None):
        if set_msg and self._rotation_msg is None:
            self._rotation_msg = set_msg
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._upd(x)
        self._upd(y)
        return y

    # ---- insert ----
    def insert(self, root, key):
        self._rotation_msg = None  # reset for this insertion
        k = int(key)
        root = self._insert_rec(root, k)
        if self._rotation_msg:
            print(self._rotation_msg)
        return root

    def _insert_rec(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.val:
            node.left = self._insert_rec(node.left, key)
        else:
            # duplicates go to the right to keep behavior deterministic
            node.right = self._insert_rec(node.right, key)

        self._upd(node)
        bf = self._bf(node)

        # LL case: right rotation
        if bf > 1 and key < node.left.val:
            return self._right_rotate(node, set_msg="Right Right Rotation")

        # LR case: left rotate left child, then right rotate
        if bf > 1 and key > node.left.val:
            node.left = self._left_rotate(node.left)  # don't set message yet
            return self._right_rotate(node, set_msg="Left Right Rotation")

        # RR case: left rotation
        if bf < -1 and key > node.right.val:
            return self._left_rotate(node, set_msg="Left Left Rotation")

        # RL case: right rotate right child, then left rotate
        if bf < -1 and key < node.right.val:
            node.right = self._right_rotate(node.right)  # don't set message yet
            return self._left_rotate(node, set_msg="Right Left Rotation")

        return node


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


# ---- driver ----
print(" *** AVL Tree Insert Element ***")
myTree = AVL_Tree()
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("====================")
