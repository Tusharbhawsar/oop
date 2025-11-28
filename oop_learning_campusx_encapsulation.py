# Encapsulation use for hide the data
# access modifier basically are words that are use in the start of the data and methods like private 
# for this operation use double underscore (__)
# we can aslo hide the methods as well show in below example
class Atm:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0      #private 
        # self._change_pin = 0    #protected
        # print("hellow")      #this will run automatically
        self.__menu()          # yaha pr menu call horha he 

    ##getter and setter methods
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if type(new_pin) == str:
            self.pin = new_pin
            print("pin changed")
        else:
            print("Not Allowed")

    def __menu(self):
        user_input = input(""" 
                    Hellow how would you like to processed?
                    1.Enter 1 create to pin
                    2.Enter 2 deposite
                    3.Enter 3 to withdraw
                    4.Enter 4 to checkbalance 
                    5.Enter 5 to exit 

""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposite()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.checkbalance()    
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("Enter the pin  ")
        print("Pin set sucessful")

    def deposite(self):
        temp = input("Enter the Deposite pin  ")
        if temp == self.__pin:
            amount = int(input("Enter the amount  "))
            self.__balance = self.__balance + amount
            print("Deposite Sucessful")
        else:
            print("Invalid Pin Please Enter Correct Pin  ")

    def withdraw(self):
        temp = input("Enter the withdraw pin  ")
        if temp == self.__pin:
            amount = int(input("Enter the amount  "))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("operation sucessful")
            else:
                print("Insuficient Funds")
        else:
            print("Invalid Pin")

    def checkbalance(self):
        temp = input("Enter the checkbalance pin  ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")   
        

sbi = Atm()                    #reference variable
# sbi.create_pin()
sbi.deposite()
sbi.withdraw()
sbi.checkbalance()
sbi.

#we can create multiple object for a class that why it called as instance 
# hdfc = Atm()
# # hdfc.create_pin()
# hdfc.deposite()
# hdfc.withdraw()
# hdfc.checkbalance()