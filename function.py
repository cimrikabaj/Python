#1. def func_name():
#     print("this is our function")
#     print("we are making new function")

# func_name()#function reference
# func_name#call by reference

#types of function
#2.with the help of function we can modularize the program and also call the function for the program
# def view_profile(name,contact):#parameters
#     print(f"Name:{name}")# by using format
#     print(f"contact:{contact}")

# view_profile("ram","984152656")#arguments(passed value)
# view_profile("shyam","5545700")

#3.function with and without written type
# def addition(num1,num2):
#     total=num1+num2
#     return total

# sum=addition(20,30)#the return value gets stored in the function we have called i.e total value gets stored in the function call addition(20,30)
# print(sum)

#4.
# def product(num1,num2):
#     res=num1*num2
#     print(f"result:{res}")

# p=product(20,2)
# print(f"result after function call:{p}")
#as there is no return the print after function call gets the result none

# def division(num1,num2):
#     div=num1/num2
#     print(f"the result is:{div}")
#     return div

# a=division(23,1)
# print(f"the result is:{a}")

#5.
#define a function which takes three numbers from its parameter and return the greatest number
# def great(num1,num2,num3):
#     if num1<=num1>=num3:
#        # print(f"num1 {num1} is greatest")
#        return num1
#     elif num2<=num3>=num1:
#         #print(f"num3 {num3} is greatest")
#         return num3
#     elif num1<=num2>=num3:
#         #print(f"num2 {num2}is greatest")
#         return num2

# g=great(8,6,8)
# print(f"the greatest is {g}")

#day6
#1.
# name=input("enter name:")
# contacts=input("enter contact:")
# address=input("enter address:")
# def display_profile(name,contact,address):
#     print(f"Name:{name}")
#     print(f"Contact:{contact}")
#     print(f"Address:{address}")

# display_profile("Ram","ktm","9841564578")#positional argument
# display_profile(name="ram",contact="9841546545",address="ktm")#keyword argument
# display_profile(name,contacts,address)#from input

#2.
# def exponent(base,power=2):#if power is not given then default power value works i.e 2 for this case
#     #default value should be at the back not front
#     return base**power;#base^power

# print(exponent(2,3))
# print(exponent(2))

#3.define a function which takes a number and return true if its even or false if its odd.tale user input amd pass that valueas am argument
# no1=int(input("enter a number:"))
# def odd_even(num1):
#     if num1 % 2==0:
#         return True
#     else:
#         return False

# print(odd_even(no1))

#Or we can do this
# def odd_even(num1):
#     return num1 % 2==0
# print(odd_even(5))

#3.define a function which calculate profit or loss based on cost price and sale price: profit=Rs.100 loss=Rs.10
# def determine(cp,sp):
#     if cp>sp:
#         return False
#     else:
#         return True

# cp=int(input("enter cost price:"))
# sp=int(input("enter selling price:"))
# a=determine(cp,sp)
# if a==True:
#     print(f"the profit is {(sp-cp)}")
# else:
#     print(f"the loss is {(cp-sp)}")

    #or 
    # def determine(cp,sp):
    #     if cp>sp:
    #         loss=cp-sp
    #         print(f"loss:Rs.{loss}")
    #     if sp>cp:
    #         profit=sp-cp
    #         print(f"profit:Rs.{profit}")



#DAY 10
# *args(postional argument), **kwargs(keyword argument)
#this are variable * contains all the meaning

# def example(a):
#     print(a)
# example(1)

# def example(*a):
#     print(a)
# example(1,2,3,4)

# def example2(**k):
#     print(k)
# example2(name="ram",address="ktm")

# def demo(*args,**kwargs):
#         print(args)
#         print(kwargs)
# demo(1,2,3,4,5,6,name="ram",address="ktm")



