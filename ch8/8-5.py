class BST:
    class BSTNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, root=None) -> None:
        self.root = root

    # Standard BST insert (no duplicates handling; duplicates go right by convention)
    def insert(self, root, key):
        if root is None:
            return BST.BSTNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    # Find and return the subtree rooted at key (without modifying the tree)
    def search_subtree(self, root, key):
        curr = root
        while curr:
            if key == curr.val:
                return curr
            elif key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None  # not found

    # Delete the entire subtree rooted at key; return the (possibly new) root of the remaining BST
    def delete_subtree(self, root, key):
        if root is None:
            return None

        # If the node to cut is the root
        if root.val == key:
            return None  # cutting the whole tree away leaves nothing

        parent = None
        curr = root
        # Search for node with value == key, keeping parent
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            # key not found; return original root unchanged
            return root

        # Cut the link from parent to this node
        if parent.left is curr:
            parent.left = None
        else:
            parent.right = None

        return root

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent, root.val)
            self.printTree90(root.left, indent + 1)


class AVLTree:
    class AVLNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
            self.height = 1  # node starts with height 1

    def __init__(self, root=None) -> None:
        self.root = root

    def get_height(self, node):
        return 0 if node is None else node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    # Standard AVL insert
    def insert(self, root, key):
        # 1) Normal BST insert
        if root is None:
            return AVLTree.AVLNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2) Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3) Get balance
        balance = self.get_balance(root)

        # 4) Balance cases
        # Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def bst_to_avl(self, bst_root):
        sorted_values = self.inorder_traversal(bst_root)
        for val in sorted_values:
            self.root = self.insert(self.root, val)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.val]
            + self.inorder_traversal(root.right)
        )

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)


# -------------------------
# Driver (reads one line)
# -------------------------
if __name__ == "__main__":
    inp1, inp2 = input("Enter the val of tree and node to cut: ").split("/")
    bst = BST()
    for i in inp1.split():
        bst.root = bst.insert(bst.root, int(i))

    print("Before cut:")
    bst.printTree90(bst.root)

    avl1, avl2 = AVLTree(), AVLTree()

    # Subtree to AVL
    print("Cutted Tree:")
    subtree_root = bst.search_subtree(bst.root, int(inp2))
    avl1.bst_to_avl(subtree_root)
    avl1.printTree90(avl1.root)

    # Remaining tree to AVL
    print("Left Tree:")
    bst.root = bst.delete_subtree(bst.root, int(inp2))
    avl2.bst_to_avl(bst.root)
    avl2.printTree90(avl2.root)
