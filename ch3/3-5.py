'''
Enter max of car / car in soi / operation : 5 / 1,2,3,4 / arrive 5
'''


class stack:
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
    
class Soi:
    def __init__(self):
        self.stackA = stack()
        self.stackB = stack()
    def run(self,instructions):
        instruction = instructions.split(' / ')
        max_car = int(instruction[0])
        cars = instruction[1].split(',')
        operation = instruction[2].split()
        for car in cars:
            self.stackA.push(int(car))

        if operation[0] == 'arrive':
            car_input = int(operation[1])
            if self.stackA.size() < max_car:
                for c in range(0,self.stackA.size()):
                    top = self.stackA.pop()
                    if top != car_input:
                        self.stackB.push(top)
                    else:
                        print(f"car {car_input} already in soi")
                        self.stackA.push(top)
                        for c in range(0,self.stackB.size()):
                            self.stackA.push(self.stackB.pop())
                        return
                for c in range(0,self.stackB.size()):
                    self.stackA.push(self.stackB.pop())
                self.stackA.push(car_input)
                print(f"car {car_input} arrive! : Add Car {car_input}")
            else:
                print(f"car {car_input} cannot arrive : Soi Full")
        
        elif operation[0] == 'depart':
            car_input = int(operation[1])
            if not self.stackA.is_empty():
                for c in range(0,self.stackA.size()):
                    top = self.stackA.pop()
                    if top != car_input:
                        self.stackB.push(top)
                    else:
                        print(f"car {car_input} depart ! : Car {car_input} was remove")
                        for c in range(0,self.stackB.size()):
                            self.stackA.push(self.stackB.pop())
                        return
            for c in range(0,self.stackB.size()):
                self.stackA.push(self.stackB.pop())
            print(f"car {car_input} cannot depart : Dont Have Car {car_input}")


print("******** Parking Lot ********")
expression = input("Enter max of car / car in soi / operation : ")
soi = Soi()
soi.run(expression)

print("[",end="")
for i in range(0,soi.stackA.size()):
    if i == soi.stackA.size() - 1:
        print(soi.stackA.items[i], end="]")
    else:
        print(soi.stackA.items[i], end=", ")  

                