class Queue:
    def __init__(self):
        self.items = []
        self.tally = 0

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        self.tally += 1

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)
    
    def queue_number(self):
        return self.tally
    


instructions = input("input : ")
instructions = instructions.split(',')
error_dequeue = 0
error_input = 0
queue = Queue()
for step in instructions:
    print(f"Step : {step}")
    if step.startswith('D'):
        num = int(step[1:])
        if queue.size() < num:
            error_dequeue += num - queue.size()
            [queue.dequeue() for _ in range(queue.size())]
            print("Dequeue : []")
        else:
            dequeued_items = [queue.dequeue() for _ in range(num)]
            print(f"Dequeue : {queue.items}")
    elif step.startswith('E'):
        num = int(step[1:])
        to_queue = ['*' + str(i+queue.queue_number()) for i in range(num)]
        for item in to_queue:
            queue.enqueue(item)
        print(f"Enqueue : {queue.items}")
    else:
        error_input += 1
        print(queue.items)
    print(f"Error Dequeue : {error_dequeue}")
    print(f"Error input : {error_input}")
    print("--------------------")