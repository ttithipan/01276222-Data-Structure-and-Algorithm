class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_head(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def delete(self, x):
        current = self.head
        prev = None
        while current:
            if current.value == x:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

commands = input("Enter Commands: ").split()

formated_command = []
for i in range(0,len(commands)//2):
    formated_command.append([commands[2*i],commands[2*i+1]])
formated_command.append(['print'])

sll = SinglyLinkedList()

for command in formated_command:
    if command[0] == "append":
        sll.append(command[1])
    elif command[0] == "insert_head":
        sll.insert_head(command[1])
    elif command[0] == "delete":
        sll.delete(command[1])
    elif command[0] == "print":
        sll.print_list()
    else:
        print(f"Unknown command: {command}")
