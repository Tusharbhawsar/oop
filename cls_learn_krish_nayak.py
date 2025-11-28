class Car:
    def __init__(self,window, doors ,enginetype):  #arguments
        self.window = window
        self.doors = doors                         #attributes
        self.enginetype = enginetype

    def driving(self):
        print("Car is used for driving")

# child class(Audi) will inheriting the parent class(Car)
class Audi(Car):
    def __init__(self, window, doors, enginetype,horsepower):
        super().__init__(window, doors, enginetype)
        self.horsepower = horsepower

    def selfdriving(self):
        print("It is self driving car")


audi7 = Audi(4,2,"Disel",200)     #this is an object

# print("this is and object:",audi7)
# print(audi7.driving())
# audi7.driving()

# print(audi7.horsepower)
# print(audi7.doors)
# print(audi7.selfdriving())

car1 = Car(2,1,"CNG")
# print(car1.doors)
# print(car1.window)
# print(car1.enginetype)

# print(dir(Car))   #car has only 1 method
print(dir(car1))
# print(dir(audi7))
