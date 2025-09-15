class queue:
    def __init__(self) -> None:
        self.current_queue = []
    def enqueue(self, element):
        self.current_queue.append(element)
        return len(self.current_queue)-1
    def dequeue(self):
        return self.current_queue.pop(0), len(self.current_queue)
    def front(self):
        return self.current_queue[0]
    def back(self):
        return self.current_queue[-1]
    def return_queue(self):
        return self.current_queue

my_queue = queue()

instruction = input("Enter Input : ")
instruction = instruction.split(',')
for iter in range(len(instruction)):
    instruction[iter] = instruction[iter].split(' ')

for each_instruction in instruction:
    if each_instruction[0] == 'E':
        print(f'Add {each_instruction[1]} index is {my_queue.enqueue(each_instruction[1])}')
    else:
        if len(my_queue.return_queue()) == 0:
            print(-1)
        else:    
            data, size = my_queue.dequeue()
            print(f'Pop {data} size in queue is {size}')

if my_queue.return_queue():
    print(f'Number in Queue is :  {my_queue.return_queue()}')
else:
    print('Empty')