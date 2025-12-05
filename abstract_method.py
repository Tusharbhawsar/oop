
# abstract clsss kya hota he jisme atlest ek abstract method hota he 
# their are two types of methods abstract method and concrete method 
# concrete method normal method hota he jisme humne normal code likha hota he
# abstract method me koi code nhi hota he sirf method ka declaration hota he

# abstract method use karte jab senior developer/top-level class lower class pr constraint lagana chahta hai ki
# ki jo bhi class isse inherit karegi usme ye methods hone chahiye warna


# Bank App example:
# BankApp (abstract class) backend database se connected hai.
# WebApp and MobileApp dono BankApp ko inherit karti hain database access ke liye.
# you are senior developer
# But senior developer force karta hai: “Security method implement karo, otherwise inherit nahi kar sakte!”

# Key Benefits (Main Use Case)
# Force implementation – Child classes ko abstract methods compulsory implement karne padte hain.
# Hide details – Actual implementation hidden rehti hai; sirf method ka existence visible hota hai.
# Large applications me consistency maintain karne ke liye perfect approach.

from abc import ABC,abstractmethod

class BankApp(ABC):        #abstract class

    def database(self):
        print("connected to database")

    @abstractmethod
    def security(self):     #abstract method
        pass

    @abstractmethod
    def display(self):      #abstract method
        pass


class MobileApp(BankApp):

    def mobile_login(self):
        print("Login into mobile")

    def security(self):
        print("mobile security")

    def display(self):
        print("display security")
    
mobile = MobileApp()
mobile.security()
mobile.display()
mobile.database()
mobile.mobile_login()

bank = BankApp()            #we cant not create object of abstract class it throws error