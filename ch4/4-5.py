class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        return self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None
    def discard(self):
        self.queue = []
        return self.queue
    def length(self):
        return len(self.queue)
    def get_queue(self):
        return self.queue
    def is_empty(self):
        if self.queue:
            return False
        else:
            return True
    
class Side(Queue):
    def __init__(self, data):
        self.bomb_count = 0
        self.bomb_item = Queue()
        self.process_queue = Queue()
        self.has_potential_bomb = True
        super().__init__()
        for i in data:
            self.enqueue(i)
        
    def get_bomb_count(self):
        return self.bomb_count
    def add_bomb_count(self):
        self.bomb_count += 1
        return 'Added Succesfully'
    
    def get_bomb_leftover(self):
        if self.is_empty():
            return False
        return self.get_queue()
    
    def bomb_checker(self):
        repeats = set()
        for i in range(len(self.get_queue()) - 2):
            if self.get_queue()[i] == self.get_queue()[i+1] == self.get_queue()[i+2]:
                repeats.add(self.get_queue()[i])
        return list(repeats)


class Game():
    def __init__(self, normal_input, mirror_input):
        self.mirror = Side(mirror_input[::-1])
        self.normal = Side(normal_input)
        self.failed_interuption = 0

    

    def output(self):
        print("NORMAL :")
        print(self.normal.length())
        if not self.normal.get_bomb_leftover():
            print('Empty')
        else:
            print(*self.normal.get_bomb_leftover()[::-1], sep='')
        
        print(self.normal.get_bomb_count(), "Explosive(s) ! ! ! (NORMAL)")
        if self.failed_interuption > 0:
            print(f'Failed Interrupted {self.failed_interuption} Bomb(s)')
        print("------------MIRROR------------")
        print(": RORRIM")
        print(self.mirror.length())
        if not self.mirror.get_bomb_leftover():
            print("ytpmE")
        else:
            print(*self.mirror.get_bomb_leftover()[::-1], sep = '')
        print("(RORRIM) ! ! ! (s)evisolpxE", self.mirror.get_bomb_count())
    
    def process(self):
        #processing mirror side
        while self.mirror.bomb_checker():
            first, second, third = self.mirror.dequeue(), self.mirror.dequeue(), self.mirror.front()
            while not self.mirror.is_empty():
                if first == second and first == third:
                    self.normal.bomb_item.enqueue(first)
                    third = self.mirror.dequeue()
                    first, second, third = self.mirror.dequeue(), self.mirror.dequeue(), self.mirror.front()
                    self.mirror.add_bomb_count()
                else:
                    third = self.mirror.dequeue()
                    self.mirror.process_queue.enqueue(first)
                    first = second
                    second = third
                    third = self.mirror.front()
            if first:
                self.mirror.process_queue.enqueue(first)
            if second:
                self.mirror.process_queue.enqueue(second)
            self.mirror.queue = self.mirror.process_queue.queue


            #print(self.normal.bomb_item.get_queue())


        #self.normal.bomb_item.queue = self.normal.bomb_item.queue[::-1]


        #processing normal side
        while self.normal.bomb_checker():
            first, second, third, stopper = self.normal.dequeue(), self.normal.dequeue(), self.normal.front(), self.normal.bomb_item.dequeue()
            #print(first,second,third,stopper)
            while not self.normal.is_empty():
                if first == second and first == third and first == stopper:
                    self.failed_interuption+=1
                    first = self.normal.dequeue()
                    second = self.normal.dequeue()
                    third = self.normal.front()
                    stopper = self.normal.bomb_item.dequeue()
                elif first == second and first == third and stopper:
                    self.normal.process_queue.enqueue(first)
                    self.normal.process_queue.enqueue(second)
                    self.normal.process_queue.enqueue(stopper)
                    
                    first = self.normal.dequeue()
                    second = self.normal.dequeue()
                    third = self.normal.front()
                    stopper = self.normal.bomb_item.dequeue()
                elif first == second and first == third:
                    self.normal.add_bomb_count()
                    third = self.normal.dequeue()
                    first = self.normal.dequeue()
                    second = self.normal.dequeue()
                    third = self.normal.front()
                else:
                    self.normal.process_queue.enqueue(first)
                    first = second
                    second = self.normal.dequeue()
                    third = self.normal.front()
            if first:
                self.normal.process_queue.enqueue(first)
            if second:
                self.normal.process_queue.enqueue(second)
            self.normal.queue = self.normal.process_queue.queue
        


normal, mirror = input("Enter Input (Normal, Mirror) : ").split()
game = Game(normal, mirror)
game.process()
game.output()

