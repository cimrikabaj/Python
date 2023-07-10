#DAY 7
#syntax:
# for <variable> in <iterable_object>:
#     code to repeat

#1.
# students=["ram","shyam","hari","sita","gita"]
# for i in students:
#     print(i)


#2.
#range(start,stop,step)
#range(10)=>start=0,stop=9,step=1
#range(1,10)=>start=1,stop=9,step=1
#range(1,10,2)=>start=1,stop=9,step=2

#print 1 to 100
# for i in range(1,101):
#     print(i)

# for i in range(0,11,2):
#     print(i)

# students=[]
# for i in range(5):
#     name=input("enter any name:")
#     students.append(name)
# print(students)


#3.
#find the sum of all element in the list a=[10,15,16,78,90]
# a=[10,23,16,78,90]
# add=0
# for i in range(0,4,1):
#     add+=i
# print(add)

#or
# total=0
# for i in a:
#     total=total+i

#print(sum(a))
#print(sum(range(2,101,2)))


#4.
#colors=["red","blue","yellow","red","green"]
#colors_to_remove=["blue","red"]
#remove colors from list of colors if it is present in colors_to remove
# for i in colors:
#     for j in colors_to_remove:
#         if i==j:
#             colors.remove(i)
# print(colors)

# result=[]
# for i in colors:
#     for j in colors_to_remove:
#         if i==j:
#             result.append(i)
# for i in range(len(result)):
#     colors.remove(result[i])
# print(colors)
    

#5.
#fruits=["apple","grapes","banana","mango","guava"]
#replace "grapes" and "banana" with "litchi"
#take user input and remove it from list of present

# for i in fruits:
#     if i=="grapes" or i=="banana":
#         a=fruits.index(i)
#         fruits.remove(i)
#         fruits.insert(a,"litchi") 
# print(fruits)

# f=input("enter any fruits name:")
# for i in fruits:
#      if i==f:
#         fruits.remove(i) 
# print(fruits)


#6.
#find the sum of odd numbers between 1 to 100
# add=0
# for i in range(1,101,2):
#     add = add +i
# print(add)

# #solution by sir
#4.
# for i in colors:
#      if i in colors_to_remove:
#         colors.remove(i)
# print(colors)

#day 8

#1
#take user input and print multiplication table
#print:5x1=5
# no=int(input("enter any number:"))
# for i in range(1,11):
#     print(f"{no}X{i}={no*i}")

#2.
# a="12d57d36d19 "#find the sum of 12,57,36 and 19
# c=a.strip().split("d")
# print(c)
# total=0
# for i in c:
#     total= total+int(i)
# print(total)

#3.
# a="387$12.45f" #find sum of all numbers in string
# total=0
# for i in a:
#     if i.isnumeric():
#         total=total+int(i)
# print(total)

#