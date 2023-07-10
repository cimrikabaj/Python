#DAY 11

#1.
# def func():
#     print("hello students")
# func()
# a=func#a hold reference of func so we can call function by either a or func
# a()
#print(a) or print(func)# to see their reference no and it comes the same

#2.
# def addition(a,b):
#     return a+b
# #print(addition(20,30))
# total=addition
# print(total(10,20))

#3.
# def outer():
#     print("i am outer function")
#     def inner():
#         print("i am inner funciton")
#     inner() 
# outer()
#inner()#does not work as it is not globally declared

#to call the inner function outside independently
# def outer():
#     #print("i am outer function")
#     def inner():
#         print("i am inner funciton")
#     return inner#function reference is returned to i
# i=outer()
# i()
# print(i)


#4.
# def outer(n):
#     def first_Child():
#         print("i am the first child")
#     def second_child():
#         print("i am the second child")
#     if n==1:
#         return first_Child
#     elif n==2:
#         return second_child

# first=outer(1)
# second=outer(2)
# first()
# second()


#5.
# def greet(func):#func=reference of welcome
#     func()#welcome function gets called
# def welcome():
#     print("welcome guys")
# def bye():
#     print("bye guys")
# greet(welcome)#welcome is passed as a reference
# greet(bye)


#DAY 12

#1.
# def calculator(operator):
#     def add(a,b):
#         return a+b
#     def diff(a,b):
#         return a-b
#     def product(a,b):
#         return a*b
#     if operator =="+":
#         return add
#     elif operator =="-":
#         return diff(
#     elif operator =="*":
#         return product
# addition=calculator("+")
# print(addition(10,20))

#2.
#return,pass and function call
#the num variable does not dissapear and remain 10 if it is given 10
# def increase_by(num):#increase_by(factor) and num is local variable it is global only if a=20 is declared at the beginnning
#     def factor(func,x,y):
#         return func(x,y)+num
#     return factor

# def exponent(x,y):
#     return x ** y
# def addition(x,y):
#     return x+y
# increase_by_ten= increase_by(10)#returns factor
# #increase_by_twenty= increase_by(20)
# print(increase_by_ten(exponent,2,5))#print(factor(exponent,2,5))
#print(increase_by_twenty(addition,2,5))

#3.
#decorator function
#
# def decorate_function(func):
#     def wrapper():
#         print("something can be done before.")
#         func()
#         print("something can be done after")
#     return wrapper

# @decorate_function
# def example():
#     print("i am example function")
# example()

#4.
#import time
# def show_timing(func):
#     def wrapper():
#         start_time=time.time()
#         result=func()
#         elapsed_time=time.time()
#         print(f"Total time taken by {func}:{elapsed_time}")
#         return result
#     return wrapper

# @show_timing#tells to call show_timing with func as multiple_of_five
# def multiple_of_five():
#     a=[]
#     for i in range(5,1000,5):
#         a.append(i)
#     return a
# print(multiple_of_five())

#5
# def smart_division(func):
#     def wraper(a,b):
#         if b==0:
#             return"could not divide by zero"
#         return func(a,b)
#     return wraper

# @smart_division#returns the reference given by smart division
# def division(a,b):
#     return a/b

# print(division(10,5))
# print(division(20,0))


#day 13

#1.
#lambda function(anomous function)
#syntax: lambda parameter:reference
#a=lambda x,  y, z : x + y + z
#print(a(10,20,0))
#used for one time use

#2.
#map,filter
#syntax: map(function,iterable object)
#alist=[1,2,3,4,5,6,7,8]
# blist=[]
# for i in alist:
#     blist.append(i+1)
# print(blist)
#1.a=map(lambda n:n+1,alist)
#print(list(a)) or print(tuple(a))
#2.
# def increment(n):
#     return n+1
# a=map(increment,alist)
# print(a)
#print(list(a))

#3.
# names=["ram","shyam","hari","gita","sita",]
# #output=["Ram","Shyam","Hari","Gita","Sita"]
# def cap(n):
#     return n.capitalize()
# a=map(cap,names)
# print(list(a))
#or
# print(list(map(lambda name:name.capitalize(),names)))

#map le harek lai rakhcha jun output huncha

#4.
#filter
#filter(func, iterable_obj)
#number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#print(list(filter(lambda n:n%2==0,number)))
#filter only return the comdition satisfied by the condition where as map displays everything also false
#print(list(map(lambda n:n%2==0,number)))

#5.
#emails=["1@gmail.com","2@look.com","3@gmail.com","2@yahoo.com"]
#print(list(filter(lambda n:n.endswith("gmail.com"),emails)))


    
#day 15

#1.
# def save(data, **kwargs):
#     if kwargs.get("commit"):
#         #logic
#     if kwargs.get("use_transc"):
#         #logic
#     database.save(data)
# print(data)

#2.
# def square_root_of_number(num):
#     return num,num**0.5
# print(square_root_of_number(25))
# num,sqr=square_root_of_number(25)

