class Spherical:
    def __init__(self,r):
        self.radius = r
        self.pi = 3.141592653589793
    def changeR(self,Radius):
        self.radius = Radius
    def findVolume(self):
        return 4/3 * self.pi * (self.radius ** 3)
    def findArea(self):
        return 4 * self.pi * (self.radius ** 2)
    def __str__(self):
        return "Radius =" + str(self.radius) + " Volumn = " + str(self.findVolume()) + " Area = " + str(self.findArea())

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(R1)
R1.changeR(int(r2))
print(R1)