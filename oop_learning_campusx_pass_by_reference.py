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

both the ids will be same


# ____________________


# class Customer:

#     def __init__(self,name):
#         self.name = name
        
# def greet(customer):
#     customer.name = "Nitesh"
#     print(customer.name)


# cust = Customer("tushar")

# # if we pass object in a function so function able to change the object variable and etc in above line
# greet(cust)

# print(cust.name)

# #class ke objects are also mutable like list,dict and sets  