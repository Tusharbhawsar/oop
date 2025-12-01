# class User:

#     def login(self):
#         print("Login")

#     def register(self):
#         print("Register")

# class Student(User): 
    
#     def enroll(self):
#         print("Enroll")

#     def review(self):
#         print("Review")

# su1 = Student()

# su1.register()
# #child class can access all the methods,contructor ,data member except __ private methods
# print(dir(su1))

# # ______________________________________________________________________________________________________
# #private methods can't access by the child class

# class User:

#     def __login(self):
#         print("Login")

#     def register(self):
#         print("Register")

# class Student(User): 
    
#     def enroll(self):
#         print("Enroll")

#     def review(self):
#         print("Review")

# su1 = Student()

# su1.__login()

# # ________________________________________________________________________________________
# # polymorphism
# # Method overriding
# # MO ka mtlab hota he parent class ke method ko child class me same ,aur same parameter ke saath define
# # karna,lekin behaviour change kar dena 


# class Phone:
#     def __init__(self,price,brand):
#         self.price = price
#         self.brand = brand

#     def buy(self):
#         print("Buying a phone")

# class Smartphone(Phone):
#     def buy(self):
#         print("Buying a smartphone")


# s = Smartphone(20000,"Oneplus")
# s.buy()   # it will call the buy method of smartphone class not phone class

#output = Buying a smartphone


# ________________________________________________________________________________________

# with the help of super() we can call the parent class method
# super() = method invoking

class Phone:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand

    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):                   #becoz of method overriding it will run first
    def buy(self):
        print("Buying a smartphone")
        super().buy()                      # it will call the buy method of parent class


s = Smartphone(20000,"Oneplus")
s.buy()     

# output = Buying a smartphone
#         Buying a phone

# ________________________________________________________________________________________
#super() = Constructor invoking


class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class Smartphone(Phone):
    print("Pehle yahan")

    def __init__(self, price, brand ,camera, os ,ram):
        super().__init__(price , brand,camera)
        self.os = os
        self.ram = ram
        print("Inside Smartphone Constructor")
    

s = Smartphone(20000,"Oneplus",12,"android",8)

print(s.os)
print(s.brand)   


#jitni bhi chize mujhe karni he (child class ko) os,ram wo me karunga , but jitni bhi chizo ke 
#liye upper code likhan hua he (parent class me) price,brand,camera wo me dubara nhi likhunga
#uske liye me constructor ko call karke apna kam karva lunga super() ki through


#_________________________________example 1_______________________________

class Parent:
    def __init__(self, num):
        self.__num = num
    
    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self, num, val):
        super().__init__(num)        #this work only here not after this line
        self.__val = val
    
    def get_val(self):
        return self.__val

son = Child(100, 200)
print(son.get_num())
print(son.get_val())

#output: 100
#        200


#_________________________________example 2_______________________________

class Parent:
    def __init__(self):
        self.num = 100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200

    def show(self):
        print(self.num)
        print(self.var)

son = Child()
son.show()
# output: 100
#         200

#kya aap child class ke ander se self ko use karke parent class ke attributes ko call 
#kar sakte ho ya nhi answer is yes

#_________________________________example 3_______________________________

class Parent:
    def __init__(self):
        self.__num = 100

    def show(self):
        print('Parent:', self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 10

    def show(self):
        print("Child:", self.__var)

dad = Parent()
dad.show()
son = Child()
son.show()

# output: Parent: 100
#         Child: 10