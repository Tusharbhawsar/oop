class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")

class Student(User): 
    
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

su1 = Student()

su1.register()
#child class can access all the methods,contructor ,data member except __ private methods
print(dir(su1))

# ______________________________________________________________________________________________________
#private methods can't access by the child class

class User:

    def __login(self):
        print("Login")

    def register(self):
        print("Register")

class Student(User): 
    
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

su1 = Student()

su1.__login()

# ________________________________________________________________________________________
# polymorphism
# Method overriding
# MO ka mtlab hota he parent class ke method ko child class me same ,aur same parameter ke saath define
# karna,lekin behaviour change kar dena 


class Phone:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand

    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):
    def buy(self):
        print("Buying a smartphone")


s = Smartphone(20000,"Oneplus")
s.buy()   # it will call the buy method of smartphone class not phone class

#output = Buying a smartphone


# ________________________________________________________________________________________

#with the help of super() we can call the parent class method

class Phone:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand

    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy()   # it will call the buy method of parent class


s = Smartphone(20000,"Oneplus")
s.buy()     

#output = Buying a smartphone
#         Buying a phone