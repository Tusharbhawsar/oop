### Decorators

# A decorator in python is a function that receives another function as input and adds some functionality(decoration) to and it and returns it.

# This can happen only because python functions are 1st class citizens.

# There are 2 types of decorators available in python
# - `Built in decorators` like `@staticmethod`, `@classmethod`, `@abstractmethod` and `@property` etc
# - `User defined decorators` that we programmers can create according to our needs


def modify(func,num):
    return func(num)

def square(num):
    return num **2

modify(square,2)

_________________________________
def my_decorator(func):

    def wrapper():
        print("********************")
        func()
        print("********************")

    return wrapper

def hello():
    print("hello")

def display():
    print("hello tushar")


a= my_decorator(hello)
a()

b = my_decorator(display)
b()

#_________________________________                  

# write the same logic in simple Code

def my_decorator(func):
    def wrapper():
        print("************")
        func()
        print("*************")

    return wrapper

@my_decorator
def hello():
    print("hello")

hello()


#create a decorator which show the amount of time taken by a function to execute

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        print("time taken by",func.__name__,time.time() -start , "secs")
    return wrapper

@timer
def hello():
    print("hello")

hello()


#in this code their is a one issue it take only one argumnet not multiple so here we are fixing this issue
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print("time taken by",func.__name__,time.time() -start , "secs")
    return wrapper

@timer
def hello():
    print("hello")

@timer
def display():
    print("displaying")

@timer
def square(num):
    print(num**num)

@timer
def cube(a,b):
    print(a**b)

hello()
display()
square(2)
cube(2,3)


#create a function that will check the input type usng decorator
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)
            else:
                raise TypeError ("ye datatype nhi chalega")
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num ** 2)

@sanity_check(str)
def greet(name):
    print("hello",name)

# square("2")
square(2)
greet("tushar")

# A basic decorator that uppercases the return value of the decorated function.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def change_upper():
    return "hello tushar"

change_upper()


#refer ipynb file for more examples