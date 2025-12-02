# 4 types of inheritance in python
# 1. Single level Inheritance
# 2. Multi-level Inheritance
# 3. Hierarchical Inheritance
# 4. Multiple Inheritance
# 5. Hybrid Inheritance

#_________________________________Single level Inheritance_______________________________

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    pass


SmartPhone(1000, "Apple", "13px").buy()
# output = inside phone constructor
#          Buying a phone

#_________________________________Multi level Inheritance_______________________________
class Product:
    def review(self):
        print("Product customer review")


class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 12)
p = Phone(1000, "Samsung", 1)

s.buy()
s.review()
p.review()
# output = Inside phone constructor
#          Inside phone constructor
#          Buying a phone
#          Product customer review
#          Product customer review
#_________________________________Hierarchical Inheritance_______________________________

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000, "Apple", "13px").buy()
                #or

s = SmartPhone(1000, "Apple", "13px")
s.buy()

# output = Inside phone constructor
#          Buying a phone
#_________________________________Multiple Inheritance_______________________________

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class Product:
    def review(self):
        print("Customer review")


class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, "Apple", 12)
s.buy()
s.review()

# output = Inside phone constructor
#          Buying a phone
#          Customer review

#_________________________________Multiple Inheritance conflict situation_______________________________

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def buy (self):
        print("Product buy method")

# class SmartPhone(Product , Phone): #it will give preference to first parent class
#     pass

class SmartPhone(Phone , Product): #it will give preference to first parent class
    pass                           # jo pehla hoga wahi preference milega  

s = SmartPhone(20000 , "Apple" , 12)
s.buy()

# output = Inside phone constructor
#          Buying a phone

