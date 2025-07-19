'''
Write a program to check if an expression has complete parentheses using a Stack to solve the problem.

The program should be able to indicate the cause of the error, if any:

Mismatched opening and closing parentheses
Excess closing parentheses
Excess opening parentheses
Then display the result according to the example.

Enter expresion : [[)))))
[[))))) Unmatch open-close  

Enter expresion : )}]
)}] close paren excess

Enter expresion : (((
((( open paren excess   3 : (((


Enter expresion : (([]))
(([])) MATCH


'''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
expression = input("Enter expresion : ")
stack = Stack()
for char in expression:
    if char in "([{":
        stack.push(char)
    elif char in ")]}":
        if stack.is_empty():
            print(f"{expression} close paren excess")
            break
        top = stack.pop()
        if (top == '(' and char != ')') or \
           (top == '[' and char != ']') or \
           (top == '{' and char != '}'):
            print(f"{expression} Unmatch open-close")
            break
else:
    if not stack.is_empty():
        print(f"{expression} open paren excess   {stack.size()} : {''.join(stack.items)}")
    else:
        print(f"{expression} MATCH")

