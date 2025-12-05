
# x : int 

# x = "ste"

# print(x)   # it will print but mypy will give error because of type hinting in above 


# # def add_num(a:int,b:int):
# #     return print(a+b)

# def add_num(a:str,b:str):   #this is annotate
#     return print(a+b)
# #now we can check all the methoda avalible in the str using a. with the helo of type hinting

# a = "er"
# b = "df"

# # a = 1
# # b = 2

# add_num(a,b)



# def add_num(a : int,b =int) ->int:
#     return a + b
#     # return "sfrfg"

# # a = "str"
# # b = "ing"
# a = 1
# b = 2

# add_num(a,b)

import typing as t

def input_data(a:t.List[str], b : t.Dict[str , int]):

    return a ,b


a = ["tushar"]
b = {"tushar": 34}

print(input_data(a,b))