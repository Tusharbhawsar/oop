class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        # print("hellow")      # this will run automatically
        self.menu()            # yaha pr menu call horha he 


    def menu(self):
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
        self.pin = input("Enter the pin  ")
        print("Pin set sucessful")

    def deposite(self):
        temp = input("Enter the Deposite pin  ")
        if temp == self.pin:
            amount = int(input("Enter the amount  "))
            self.balance = self.balance + amount
            print("Deposite Sucessful")
        else:
            print("Invalid Pin Please Enter Correct Pin  ")

    def withdraw(self):
        temp = input("Enter the withdraw pin  ")
        if temp == self.pin:
            amount = int(input("Enter the amount  "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("operation sucessful")
            else:
                print("Insuficient Funds")
        else:
            print("Invalid Pin")

    def checkbalance(self):
        temp = input("Enter the checkbalance pin  ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")   
        

# sbi = Atm()
# # sbi.create_pin()
# sbi.deposite()
# sbi.withdraw()
# sbi.checkbalance()


#we can create multiple object for a class that why it called as instance 
hdfc = Atm()
# hdfc.create_pin()
hdfc.deposite()
hdfc.withdraw()
hdfc.checkbalance()