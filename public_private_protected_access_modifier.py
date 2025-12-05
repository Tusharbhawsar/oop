#why we need access modifiers?
#to restrict access of certain methods and data members from outside the class
#ex:- passwords , sensitive data
#ex2:- i create a library and dont want user to access certain methods or data members directly

#____________________________Public modifier_____________________________
# ✔ Accessible from anywhere
# ✔ No underscore prefix
# ✔ Most common type
# Example:

class Demo:
    def _init_(self):
        self.name = "Vikash"   # public

obj = Demo()
print(obj.name)    # ✅ Allowed


# ____________________________Protected modifier_____________________________
# 2. Protected (_single_underscore)
# ✔ Accessible inside the class and subclasses
# ✔ Should NOT be accessed directly from outside (recommended, but not enforced)
# ✔ Used for internal use

# Example:

class Demo:
    def _init_(self):
        self._email = "test@example.com"  # protected

obj = Demo()
print(obj._email)    # ⚠️ Allowed but NOT recommended


# Protected in Python = soft protection (just a warning).

# ____________________________Private modifier_____________________________

#  Private (__double_underscore)
# ✔ Name-mangled → cannot be accessed directly
# ✔ Only accessible inside the class
# ✔ Used for sensitive data

# Example:

class Password():
    def __init__(self):
        self.__password = "Admin123"
    
    def __passa(self):
        return self.__password
        
        
obj = Password()

# How to access private?
# Python "name-mangles" private variables:


print(obj._Password__passa())

# print(obj._Password__passa())
