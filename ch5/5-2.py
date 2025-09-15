class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return "->".join(values)

    def str_reverse(self):
        values = []
        current = self.head
        if not current:
            return ""

        while current.next:
            current = current.next

        while current:
            values.append(str(current.data))
            current = current.previous
        return "->".join(values)

    def isEmpty(self):
        return self.head is None

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.previous = current

    def prepend(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            return

        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        length = self.get_length()
        if index < 0 or index > length:
            print("Data cannot be added")
            return

        print(f"index = {index} and data = {data}")

        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        current_index = 0

        while current_index < index - 1:
            current = current.next
            current_index += 1

        new_node.next = current.next
        new_node.previous = current

        if current.next:
            current.next.previous = new_node
        current.next = new_node

    def remove(self, data):
        if self.isEmpty():
            print("Not Found!")
            return None, -1

        current = self.head
        index = 0

        # Check head node first
        if current.data == data:
            self.head = current.next
            if self.head:
                self.head.previous = None
            return current, 0

        while current:
            if current.data == data:
                if current.previous:
                    current.previous.next = current.next
                if current.next:
                    current.next.previous = current.previous
                return current, index
            current = current.next
            index += 1

        print("Not Found!")
        return None, -1


# =========================
# Main Code (Input Parsing)
# =========================

dll = DoublyLinkedList()

user_input = input("Enter Input : ").split(',')

for command in user_input:
    command = command.strip()
    if command.startswith("A "):
        data = int(command[2:])
        dll.append(data)
        print(f"linked list : {dll}")
        print(f"reverse : {dll.str_reverse()}")

    elif command.startswith("Ab "):
        data = int(command[3:])
        dll.prepend(data)
        print(f"linked list : {dll}")
        print(f"reverse : {dll.str_reverse()}")

    elif command.startswith("I "):
        idx_data = command[2:].split(':')
        index = int(idx_data[0])
        data = int(idx_data[1])
        dll.insert(index, data)
        print(f"linked list : {dll}")
        print(f"reverse : {dll.str_reverse()}")

    elif command.startswith("R "):
        data = int(command[2:])
        removed_node, index = dll.remove(data)
        if removed_node:
            print(f"removed : {removed_node.data} from index : {index}")
        print(f"linked list : {dll}")
        print(f"reverse : {dll.str_reverse()}")

