class Customer:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == "Male":
        print("hello",customer.name , "sir")
    else:
        print("hello",customer.name, "Ma'am")



# cust = Customer("tushar","Male")
cust = Customer("Prachi","Female")


greet(cust)

# print(id(cust))

# it work lik aliasing 

a = 3
b = a

print(id(a))
print(id(b))

# both the ids will be same