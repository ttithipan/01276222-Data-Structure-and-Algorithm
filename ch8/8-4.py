class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)


# ---------------- AVL core ----------------
def h(node):
    return 0 if node is None else node.height

def update(node):
    node.height = 1 + max(h(node.left), h(node.right))
    return node.height

def bf(node):
    return h(node.left) - h(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update(y)
    update(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update(x)
    update(y)
    return y

def rebalance(node):
    update(node)
    balance = bf(node)

    # LL
    if balance > 1 and bf(node.left) >= 0:
        return rotate_right(node)
    # LR
    if balance > 1 and bf(node.left) < 0:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    # RR
    if balance < -1 and bf(node.right) <= 0:
        return rotate_left(node)
    # RL
    if balance < -1 and bf(node.right) > 0:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.val:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return rebalance(node)

def _min_node(n):
    while n.left is not None:
        n = n.left
    return n

def delete(node, key):
    if node is None:
        return None
    if key < node.val:
        node.left = delete(node.left, key)
    elif key > node.val:
        node.right = delete(node.right, key)
    else:
        if node.left is None or node.right is None:
            node = node.left if node.left is not None else node.right
        else:
            succ = _min_node(node.right)
            node.val = succ.val
            node.right = delete(node.right, succ.val)
    if node is None:
        return None
    return rebalance(node)


# ---------------- Pretty level printer ----------------
def print_levels(root):
    if root is None:
        return

    levels = root.height
    queue = [root]

    for level in range(1, levels + 1):
        next_q = []
        left_pad = 1 + ((1 << (levels - level + 1)) - 1) * 2
        between  = 1 + ((1 << (levels - level + 2)) - 1) * 2

        # enqueue children for the next level (keep Nones for structure)
        for n in queue:
            if n is None:
                next_q.extend([None, None])
            else:
                next_q.append(n.left)
                next_q.append(n.right)

        # RENDER: compress out Nones for this level's printed line
        printable = [n for n in queue if n is not None]
        if not printable:
            break  # nothing real to print on this level

        line = " " * left_pad
        first = True
        for n in printable:
            if not first:
                if n.val >= 10:
                    line += " " * (between -1)
                else:
                    line += " " * (between -1)
            first = False
            line += str(n.val)
            if n.val < 10:
                line += " "
        print(line)

        queue = next_q

        # stop if next level has no real nodes
        if all(x is None for x in queue):
            break


# ---------------- Driver ----------------
print(" *** AVL Tree ***")
nums = list(map(int, input("Enter numbers to insert: ").split()))

root = None
for x in nums:
    root = insert(root, x)

# show once after all insertions
print_levels(root)

# repeatedly delete current root and print
first = True
while root is not None:
    root = delete(root, root.val)
    if root is not None:
        print("------------------------------")
        print_levels(root)
print("------------------------------")
print("===== End of program =====")
