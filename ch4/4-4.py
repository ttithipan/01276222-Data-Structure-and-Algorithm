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
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
class Barista(Queue):
    def __init__(self):
        super().__init__()
        self.time_to_process = 0
        self.queue_time = 0

MainQueue = Queue()
barista1 = Barista()
barista2 = Barista()

print(" ***Cafe***")
log = input("Log : ")
log = log.split('/')
log = [x.split(',') for x in log]
log = [[int(x) for x in sublist] for sublist in log]
for i in range(len(log)):
    log[i].append(i+1) # Add index to each log entry


time = 1
for entry in log:
    MainQueue.enqueue(entry)

# To store coffee serve events: (time, customer_number)
coffee_events = []

# To track wait times: {customer_index: wait_time}
wait_times = dict()

while not MainQueue.is_empty() or not barista1.is_empty() or not barista2.is_empty():
    # Assign new customer to barista1 if free and customer has arrived (arrival time < current time)
    while barista1.size() < 1 and not MainQueue.is_empty() and MainQueue.front()[0] < time:
        entry = MainQueue.dequeue()
        barista1.enqueue(entry)
        barista1.time_to_process = entry[1]
        barista1.queue_time = 0
        # Record wait time for this customer
        wait_times[entry[2]] = time - entry[0]
    # Assign new customer to barista2 if free and customer has arrived (arrival time < current time)
    while barista2.size() < 1 and not MainQueue.is_empty() and MainQueue.front()[0] < time:
        entry = MainQueue.dequeue()
        barista2.enqueue(entry)
        barista2.time_to_process = entry[1]
        barista2.queue_time = 0
        # Record wait time for this customer
        wait_times[entry[2]] = time - entry[0]


    # Process barista1
    if not barista1.is_empty():
        barista1.queue_time += 1
        if barista1.queue_time == barista1.time_to_process:
            served = barista1.dequeue()
            coffee_events.append((time, served[2]))
            barista1.queue_time = 0
            barista1.time_to_process = 0
            # Immediately assign next customer if available and has already arrived
            while barista1.size() < 1 and not MainQueue.is_empty() and MainQueue.front()[0] < time:
                entry = MainQueue.dequeue()
                barista1.enqueue(entry)
                barista1.time_to_process = entry[1]
                barista1.queue_time = 0
                wait_times[entry[2]] = time - entry[0]

    # Process barista2
    if not barista2.is_empty():
        barista2.queue_time += 1
        if barista2.queue_time == barista2.time_to_process:
            served = barista2.dequeue()
            coffee_events.append((time, served[2]))
            barista2.queue_time = 0
            barista2.time_to_process = 0
            # Immediately assign next customer if available and has already arrived
            while barista2.size() < 1 and not MainQueue.is_empty() and MainQueue.front()[0] < time:
                entry = MainQueue.dequeue()
                barista2.enqueue(entry)
                barista2.time_to_process = entry[1]
                barista2.queue_time = 0
                wait_times[entry[2]] = time - entry[0]


    time += 1 

# Find the customer who waited the longest
if wait_times:
    # Print sorted coffee events
    coffee_events.sort(key=lambda x: (x[0], x[1]))
    for t, cust in coffee_events:
        print(f"Time {t} customer {cust} get coffee")
    max_customer = max(wait_times, key=lambda k: wait_times[k])
    max_wait = wait_times[max_customer]
    if max_wait == 1:
        print("No waiting")
    else:
        print(f"The customer who waited the longest is : {max_customer}")
        print(f"The customer waited for {max_wait} minutes")

    
