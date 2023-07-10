# def func():
#     print("aalu khau")
# a=func
# a()
# print(a)

# def add(a,b):
#     return a+b
# print(add(20,30))
# total=add
# print(total(10,10))

# def outer():
#     print("hello i am outer")
#     def inner():
#         print("hello i am inner")
#     inner()
# outer()

# def outer():
#     #print("i am outer")
#     def inner():
#         print("i am inner")
#     return inner
# i=outer()
# i()
# print(i)
# print(outer)

# def outer(n):
#     def first_child():
#         print("i am first child")
#     def second_child():
#         print("i am second child")
#     if n==1:
#         return first_child
#     elif n==2:
#         return second_child
# first=outer(2)
# first()
# print(first)

# def greet(func):
#     func()
# def welcome():
#     print("welcome guys")
# greet(welcome)

#1.
#0,1,1,2,3,5.....nth term
# num=int(input("Enter the term upto which u want to generate::"))
# #c=[]
# a=0
# b=1
# for i in range(0,num):
#     if i==0:
#         n=0
#     if i>=1:
#         n= a+ b
#         b=a
#         a=n
#     print(a)

#3. x=[a,b,c,d]  y=[b,c,d,a] same or not (content)

#2.palindrome
a=input("enter any word:")
for i in a:
    if i==a[0]:
        b[n]=i
    else:
        
