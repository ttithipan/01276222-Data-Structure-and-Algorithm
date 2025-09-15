class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)
    
MainQueue = Queue()
Cashier1Queue = Queue()
Cashier2Queue = Queue()

people = input("Enter people : ")
for person in people:
    MainQueue.enqueue(person)

minute = 0
time_since_last_cashier1 = 0
time_since_last_cashier2 = 0
while not MainQueue.is_empty():


    if time_since_last_cashier1 == 3:
        Cashier1Queue.dequeue()
        time_since_last_cashier1 = 0
    if time_since_last_cashier2 == 2:
        Cashier2Queue.dequeue()
        time_since_last_cashier2 = 0


    if Cashier1Queue.size() < 5:
        Cashier1Queue.enqueue(MainQueue.dequeue())
    elif Cashier2Queue.size() < 5:
        Cashier2Queue.enqueue(MainQueue.dequeue())
        
    
    minute += 1
    if not Cashier1Queue.is_empty():
        time_since_last_cashier1 +=1
    if not Cashier2Queue.is_empty():
        time_since_last_cashier2 +=1
    print(minute, MainQueue.items, Cashier1Queue.items, Cashier2Queue.items)


