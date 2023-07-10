#syntax:
#while <condition>: #condition is either true or false
    #code to repeat

#1
# a=1
# while a<10:
#     print("this is python class")
#     a=a+1

#2
# username="ram@gmail.com"
# password="abc@12345"
#ask for user input until username amd password matches to given username and password if matches then exit the loop
# usern=input("enter your username:")
# pw=input("enter your password:")
# while username!=usern or password!=pw:
#     usern=input("enter your username:")
#     pw=input("enter your password:")

#3.
# main=[]
# even=[]
# odd=[]
# duplicate=[]
#take 12 user input as interger, add all input into main list
# add even numbers to even list, add odd numbers to odd list, 
# add duplicate entry ny users into duplicate list
# main list should contain all 15 input
# whereas even and odd should not contain any duplicates
# i=0
# while i<13:
#     a=int(input("enter integers:"))
#     main.append(a)
#     if a % 2==0:
#         if a not in even:
#             even.append(a)
#     if a % 2!=0:
#         if a not in odd:
#             odd.append(a)
#     if main.count(a)>1:
#         duplicate.append(a)

#     i=i+1
# print("main:",main)
# print("even:",even)
# print("odd:",odd)
# print("duplicate:",duplicate)

#solution by sir
# for i in range(15):
#     num = int(input("Enter number: "))
#     if num not in main:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
#     else:
#         duplicate.append(num)
#     main.append(num)
# print(f"Main: {main}")
# print(f"Even: {even}")
# print(f"Odd: {odd}")
# print(f"Duplicate: {duplicate}")


#4
#break,continue

# for i in range(1,10):
#     print(i)
#     if i % 6 ==0:
#         break#break skips everything after that specific condition
#     print(i)

# for i in range(1,10):
#     if i % 6 ==0:
#         continue#continue skips that specific condition 
#     print(i)


#5
# for i in range(5):
#     print(i)
# else:
#     print("loop completed")
# #------------------------------------------------------------------------
# for i in range(5):
#     if i%3==0:
#         break
#     print(i)
# else:
#     print("loop completed")

#6.
#emails=[]
#take email as the user input for 10 times, 
# append to emails and print them, 
# if domain name of email is gmail.com

# for i in range(10):
#     e=input("enter any email:")
#     if e.endswith("gmail.com"):
#         emails.append(e)
# print(f"emails:{emails}")

#7
#tuples
# a=(1,2,3,4,5)
# type(a)
# dir(tuple)=> 'count', 'index'
#list dynamically grow huncha so more space



