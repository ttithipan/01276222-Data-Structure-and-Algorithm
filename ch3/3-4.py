'''
Write a class calculator that operates through the function run(instructions) with the following instructions:

+: Pop 2 values from the stack, add them, and push the result onto the stack.
-: Pop 2 values from the stack, subtract the top value from the second value, and push the result onto the stack.
*: Pop 2 values from the stack, multiply them, and push the result onto the stack.
/: Pop 2 values from the stack, divide the second value by the top value, and push the result onto the stack.
DUP: Duplicate (not double) the top value of the stack.
POP: Pop the top value from the stack and discard it.
PSH: Push a number onto the stack.
Note: Any other instructions (such as letters) should result in "Invalid instruction: [instruction]".


Test cases:
* Stack Calculator *
Enter arguments : 5 6 +
11


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

class Calculator:
    def __init__(self):
        self.stack = Stack()

    def run(self, instructions):
        for instruction in instructions.split():
            if instruction.isdigit():
                self.stack.push(int(instruction))
            elif instruction == '+':
                if self.stack.size() < 2:
                    print("Invalid operation: Not enough values in stack")
                    return
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a + b)
            elif instruction == '-':
                if self.stack.size() < 2:
                    print("Invalid operation: Not enough values in stack")
                    return
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a - b)
            elif instruction == '*':
                if self.stack.size() < 2:
                    print("Invalid operation: Not enough values in stack")
                    return
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a * b)
            elif instruction == '/':
                if self.stack.size() < 2:
                    print("Invalid operation: Not enough values in stack")
                    return
                a = self.stack.pop()
                b = self.stack.pop()
                if a == 0:
                    print("Invalid operation: Division by zero")
                    return
                self.stack.push(a / b)
            elif instruction == 'DUP':
                if not self.stack.is_empty():
                    top_value = self.stack.peek()
                    self.stack.push(top_value)
            elif instruction == 'POP':
                if not self.stack.is_empty():
                    self.stack.pop()
            else:
                print(f"Invalid instruction: {instruction}")
                return

        if not self.stack.is_empty():
            print(f"{self.stack.peek():.0f}")
        else:
            print("0")

print("* Stack Calculator *")
expression = input("Enter arguments : ")
calc = Calculator()
calc.run(expression)