
class Person():
    counter = 1  # static/class variable always defined outside constructor
    def __init__(self, city, pin_code, state):
        #this all are instance variables bcoz they are defined inside constructor
        self.city = city
        self.pin_code = pin_code
        self.state = state

        # self.id = self.increment_id()  #counter implementation
                #or
        self.id = Person.counter
        Person.countter += 1
        
    
    @classmethod
    def increment_id(classmethod):
        classmethod.counter += 1
        return classmethod.counter
            
        
    def print_address(self):
        data = f"City : {self.city} | PinCode : {self.pin_code} | State : {self.state} | ID : {self.id}"
        return print(data)
        

# obj1 = Person("Indore", "452010", "MP")
# obj1.print_address()

# obj1 = Person("Ratlam", "457132", "MP")
# obj1.print_address()

# we can access class variable using object also for seeing the counter value
# obj1.id
# obj2.id






#__________________________Explanation of @classmethod vs normal method_____________________________

# Here’s the clear difference with and without @classmethod in your code context.

# ✅ 1. What @classmethod does in your code

# Your method:

# @classmethod
# def increment_id(cls):
#     cls.counter += 1
#     return cls.counter

# ✔ Key points

# It receives cls, not self.

# cls refers to the class itself (Person), not the object.

# So cls.counter means Person.counter, a single shared value for all objects.

# This method can be called by:

# class → Person.increment_id()

# object → obj.increment_id()

# Both ways update the same class variable.

# ✅ 2. What happens if you remove @classmethod?

# If you change it to a normal method:

# def increment_id(self):
#     self.counter += 1
#     return self.counter

# ❌ Problems that occur:
# 🔹 Problem 1:

# counter becomes object-level instead of shared.

# Each object would have its own counter, so every object starts from 0.

# Example:

# obj1.id = obj1.increment_id()  # becomes 1
# obj2.id = obj2.increment_id()  # becomes 1 again


# Both IDs will be 1, which is WRONG for unique IDs.

# 🔹 Problem 2:

# You are modifying self.counter, not Person.counter.

# Python will create a new instance variable counter:

# obj1.counter = 1
# obj2.counter = 1


# The class-level counter (Person.counter) never changes.

# 📌 Summary Table
# Feature	With @classmethod	Without @classmethod
# Receives	cls (class)	self (object)
# Accesses	Class variable	Instance variable
# Counter shared?	Yes	No
# IDs generated	1, 2, 3, ...	Always 1, 1, 1...
# Correct for unique ID?	Yes	No
# 📌 Why your code NEEDS @classmethod

# Because you want one counter shared by all objects, so each new Person gets a unique ID.