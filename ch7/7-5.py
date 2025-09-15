# Build an expression tree from a postfix string, then print:
# - the tree rotated 90 degrees
# - the fully parenthesized infix expression
# - the prefix expression

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def build_expr_tree_from_postfix(postfix: str):
    ops = set("+-*/")
    stack = []
    for ch in postfix:
        if ch == ' ':
            continue
        if ch not in ops:
            # operand
            stack.append(Node(ch))
        else:
            # operator: pop right then left
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            right = stack.pop()
            left = stack.pop()
            op_node = Node(ch)
            op_node.left = left
            op_node.right = right
            stack.append(op_node)
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]

def to_infix(node: Node) -> str:
    if node.left is None and node.right is None:
        return str(node.data)
    # fully parenthesized
    return f"({to_infix(node.left)}{node.data}{to_infix(node.right)})"

def to_prefix(node: Node) -> str:
    if node is None:
        return ""
    return f"{node.data}{to_prefix(node.left)}{to_prefix(node.right)}"

# ---- Driver ----
postfix = input("Enter Postfix : ").strip()
root = build_expr_tree_from_postfix(postfix)

print("Tree :")
printTree90(root)
print("-" * 50)
print("Infix :", to_infix(root))
print("Prefix :", to_prefix(root))
