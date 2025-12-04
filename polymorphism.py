# Polymorphism = multiple phases 
# 1. Method overridding
# 2. Method overloading
# 3. Method Overloading

# polymorphism
# Method overriding
# MO ka mtlab hota he parent class ke method ko child class me same ,aur same parameter ke saath define
# karna,lekin behaviour change kar dena 

#___________________method overridding_______________

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
s.buy()   # it will call the buy method of smartphone class not phone class becoz of method overriding

# output = Buying a smartphone 



#___________________method overloading_______________

# Method overloading means defining multiple functions with the same name but different parameters.
# It allows you to use one function name for similar tasks while varying inputs.
# 💡 But note:
# Python does NOT support method overloading the same way Java or C++ does.

# 1. Using default parameters

class Geometry:
    def area (self,a,b = 0):
        if b == 0:
            print("Circle",3.14 * a *a)
        else:
            print("Rect",a * a)

obj = Geometry()
obj.area(4)
obj.area(4,5)


#___________________operator overriding_______________
# Operator overloading means giving special meaning to Python operators (+, -, *, ==, etc.) for our own classes.

# Python allows classes to define how operators behave when used with their objects.

# Example:
# 3 + 5 works because Python knows how to add integers.
# But if you create your own class, Python doesn’t know how to add two objects of that 
# class — unless you overload the operator.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = p1 + p2   # operator overloading in action

print(p3.x, p3.y)
# 4 6

# ✔️ Common magic methods for operator overloading
# Operator	Method
# -	        __sub__
# +	        __add__
# *	        __mul__
# /	        __truediv__
# ==	    __eq__
# <	        __lt__
# >	        __gt__
