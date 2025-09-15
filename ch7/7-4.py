class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(r, v):
            if r is None:
                return Node(v)
            if v < r.data:
                r.left = _insert(r.left, v)
            else:
                r.right = _insert(r.right, v)
            return r
        self.root = _insert(self.root, val)

    def delete(self, r, data):
        """Return (new_root, deleted_flag)."""
        if r is None:
            return (None, False)
        if data < r.data:
            r.left, deleted = self.delete(r.left, data)
            return (r, deleted)
        elif data > r.data:
            r.right, deleted = self.delete(r.right, data)
            return (r, deleted)
        else:
            # Found node to delete
            if r.left is None and r.right is None:
                return (None, True)
            if r.left is None:
                return (r.right, True)
            if r.right is None:
                return (r.left, True)
            # Two children: replace with inorder successor
            succ_parent = r
            succ = r.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            r.data = succ.data
            # Delete successor node
            if succ_parent == r:
                succ_parent.right, _ = self.delete(succ_parent.right, succ.data)
            else:
                succ_parent.left, _ = self.delete(succ_parent.left, succ.data)
            return (r, True)

def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

# --- Driver ---
tree = BinarySearchTree()
data = input("Enter Input : ").split(",")

for token in data:
    token = token.strip()
    if not token:
        continue
    op, val = token.split()
    x = int(val)

    if op == 'i':
        print(f"insert {x}")
        tree.insert(x)
        printTree90(tree.root)
    elif op == 'd':
        print(f"delete {x}")
        tree.root, deleted = tree.delete(tree.root, x)
        if not deleted:
            print("Error! Not Found DATA")
        # Always print the tree (prints nothing if empty)
        printTree90(tree.root)
