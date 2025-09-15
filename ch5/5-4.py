class Node:
    def __init__(self, word=None):
        self.word = word
        self.prev = None
        self.next = None

class TextEditor:
    def __init__(self):
        self.head = Node()  # sentinel head
        self.tail = Node()  # sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail  # cursor points to node after cursor position
    
    def insert_word(self, word):
        new_node = Node(word)
        prev_node = self.cursor.prev
        
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.cursor
        self.cursor.prev = new_node
        
        # Move cursor after inserted word
        self.cursor = new_node.next
    
    def move_left(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev
    
    def move_right(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next
    
    def backspace(self):
        if self.cursor.prev != self.head:
            to_delete = self.cursor.prev
            before = to_delete.prev
            before.next = self.cursor
            self.cursor.prev = before
    
    def delete(self):
        if self.cursor != self.tail:
            to_delete = self.cursor
            after = to_delete.next
            to_delete.prev.next = after
            after.prev = to_delete.prev
            self.cursor = after
    
    def get_text_with_cursor(self):
        result = []
        node = self.head.next
        
        while node != self.tail:
            if node == self.cursor:
                result.append('|')
            result.append(node.word)
            node = node.next
        
        # Cursor at end
        if self.cursor == self.tail:
            result.append('|')
        
        return ' '.join(result)

def text_editor_linkedlist_words(commands_input):
    editor = TextEditor()
    commands = [cmd.strip() for cmd in commands_input.split(',')]
    
    for cmd in commands:
        if cmd.startswith('I '):
            word = cmd[2:]
            editor.insert_word(word)
        else:
            if cmd == 'L':
                editor.move_left()
            elif cmd == 'R':
                editor.move_right()
            elif cmd == 'B':
                editor.backspace()
            elif cmd == 'D':
                editor.delete()
    
    return editor.get_text_with_cursor()

# Testing with your sample test cases from the prompt:
print(text_editor_linkedlist_words(input("Enter Input : ")))