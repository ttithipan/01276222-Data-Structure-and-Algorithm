class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Add a node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    # Clone the linked list
    def clone(self):
        cloned_list = LinkedList()
        current = self.head
        while current:
            cloned_list.append(current.data)
            current = current.next
        return cloned_list
    
    # Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
    def display_reverse(self):
        stack = []
        temp = self.head
        while temp:
            stack.append(temp.data)
            temp = temp.next
        while stack:
            print(stack.pop(), end=" -> " if stack else "")

    # Clear the linked list
    def clear(self):
        self.head = None
    
    # Convert the linked list into a Python list (for easy manipulation)
    def to_list(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result
    
    # Rebuild the linked list from a Python list
    def from_list(self, data):
        self.clear()
        for value in data:
            self.append(value)

    def is_zero(self):
        current = self.head
        while current and current.next:
            if current.data != 0:
                return False
            current = current.next
        return True

def split_linked_list(linked_list):
    # Create two new linked lists for positive and negative numbers
    positive_list = LinkedList()
    negative_list = LinkedList()
    
    # Traverse through the original linked list
    current = linked_list.head
    while current:
        if current.data >= 0:
            positive_list.append(current.data)  # Append positive numbers
        else:
            negative_list.append(current.data)  # Append negative numbers
        current = current.next
    
    # Return the two linked lists
    return positive_list, negative_list

def radix_sort(linked_list):
    # Get the largest absolute number to determine how many digits we need to sort
    max_value = max(linked_list.to_list(), key=abs)
    digits_count = len(str(abs(max_value)))
    
    # Perform radix sort for each digit place (starting from the least significant digit)
    for pos in range(1, digits_count + 1):
        # Create 10 buckets (one for each digit 0-9)
        buckets = [LinkedList() for _ in range(10)]
        
        # Step 1: Distribute elements into corresponding buckets based on the current digit
        current = linked_list.head
        while current:
            # Absolute value is used for sorting in radix sort
            digit = (abs(current.data) // 10 ** (pos - 1)) % 10
            buckets[digit].append(current.data)
            current = current.next
        
        # Step 2: Display the contents of each bucket (positive first, then negative)
        print("------------------------------------------------------------")
        print(f"Round : {pos}")
        
        # For each bucket 0 to 9, display positive numbers first, then negative numbers
        for i in range(10):
            positive = []
            negative = []
            temp = buckets[i].head
            while temp:
                if temp.data >= 0:
                    positive.append(temp.data)
                else:
                    negative.append(temp.data)
                temp = temp.next
            
            # Display positive numbers first
            if positive:
                print(f"{i} :", " ".join(map(str, positive)),end = '')
            else:
                print(f"{i} :", end="")
            
            # Display negative numbers next, followed by empty string
            if negative:
                print("", " ".join(map(str, negative[::-1])), end = '')
            print()  # Newline after each bucket display
        
        # Step 3: Rebuild the list from the buckets in reverse order (descending)
        linked_list.clear()
        for i in range(9, -1, -1):  # Start from 9 down to 0 for descending order
            current = buckets[i].head
            while current:
                linked_list.append(current.data)
                current = current.next

    return linked_list, pos

# Test the implementation
data = [int(x) for x in input("Enter Input : ").split()]
linked_list = LinkedList()
for value in data:
    linked_list.append(value)

# Display the data before sorting
before = linked_list.clone()

# Perform Radix Sort in one step
if linked_list.is_zero():
    print("------------------------------------------------------------")
    print("0 Time(s)")
    print(f"Before Radix Sort : ", end="")
    before.display()
    print()
    print(f"After  Radix Sort : ", end="")
    before.display()
else:
    linked_list, pos = radix_sort(linked_list)
    positive, negative = split_linked_list(linked_list)
    print("------------------------------------------------------------")
    print(f"{pos} Time(s)")
    print(f"Before Radix Sort : ", end="")
    before.display()
    print()
    print(f"After  Radix Sort : ", end="")
    positive.display()
    if negative.head:
        print(" -> ", end="")
    negative.display_reverse()

