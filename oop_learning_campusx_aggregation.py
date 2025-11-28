class Customer:
    #1step
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    #6th step
    def edit_profile(self,new_name,new_city,new_pincode,new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pincode,new_state)

class Address:
    #2nd step
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state
    #5rd step
    def change_address(self,new_city,new_pincode,new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state

#4step
add = Address("indore",452005,"mp")
#3step
cust = Customer("tushar","male",add)

print(cust.address.city)

cust.edit_profile("ritik","Mini Mumbai",452006,"mp")

print(cust.address.city)
print(cust.name)