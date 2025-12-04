#why we need access modifiers?
#to restrict access of certain methods and data members from outside the class
#ex:- passwords , sensitive data
#ex2:- i create a library and dont want user to access certain methods or data members directly


class Person():
    counter = 0
    def __init__(self, city, pin_code, state):
        self.city = city
        self.pin_code = pin_code
        self.state = state
        self.id = self.increment_id()
        
    
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


class Password():
    def __init__(self):
        self.__password = "Admin123"
    
    def __passa(self):
        return self.__password
        
        
obj = Password()
print(obj._Password__passa())