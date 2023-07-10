#class and object, encapsulation, abstraction, polymorphism, encapsulation

#day 15

#1
# class int:
#     pass 
# a=int(10)#object is 10
#a is variable pointing that object

#2.
# class Car:
#     pass
#or
# class Car:
#     pass
# print(Car())
# c=Car()#a=10

#class Car:
    #initializer function
    #def __init__(self,colors,years):#special function 
        #pass
# c=Car()#c le car bhane obj lai point gareko cha
# c.color="red"
# c.year="2020"
# print(c.color)
# print(c.year)

# def __init__(self,colors,years):#special function 
#         self.color=colors
#         self.year=years
# c=Car("red","2020")#c le car bhane obj lai point gareko cha
# print(c.colors)
# print(c.years)

#4.
#passes the value to self of above function
# def __new__(cls):#constructor
#      pass

#5.
#     def __init__(self,color,year):#special function 
#             self.color=color
#             self.year=year
#     def ride(self):
#           print(f"car of color {self.color} is riding")
# scorpio=Car("red","2020")
# bolero=Car("black","2023")
# fortuner=Car("silver","2022")
# print(scorpio.color)
# print(bolero.year)
# fortuner.ride()

#day 16

#1.
#method=>class bhitra banayeko function
#instance=>object
# class Printer:
#     def __init__(self,num_of_pages,model):
#         #instance variable
#         self.model = model
#         self.num_of_pages = num_of_pages
#     def paper_print(self):#instance method#self ko thau ma obj aucha class ko
#         print(f"{self.model} is printing {self.num_of_pages} pages.")
# p=Printer(10,"Brother DW4")
# p.paper_print()

#2.
#laptop:color,model,ram:start(),shut_down()
# class Laptop:
#     company="Lenovo"#class  variavle-> can be used by obj and class both
#     def __init__(self,color,model,ram):
#         self.color = color
#         self.model = model
#         self.ram = ram
#     def start(self):
#         print(f"the laptop{self.model} with color {self.color} with ram {self.ram} is starting of {self.company}{Laptop.company}")
#     def shutdown(self):
#         print(f"the laptop{self.model} with color {self.color} with ram {self.ram} is shutting down")
# l=Laptop("silver","dell","12")
# print(l.company)
# l.shutdown()
# l.start()

#3.
# class Calculator:
#     def __init__(self, x:int, y:int) -> None:
#         self.x = x
#         self.y = y
#     def add(self):
#         return self.x + self.y
#     def product(self):
#         return self.x * self.y
#     @staticmethod
#     #instance pass bhayeko chaina->staticmethod
#     def square_root(num):#static method
#         return num ** 0.5
# c=Calculator(15,1)
# print(c.add())
# print(c.product())
# print(Calculator.square_root(25))#for static method

#data hiding process(attribute)
# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#         #_=protected
#         #__=private
#     @property#direct function ko rup ma access garna parcha
#     def price(self):
#         return self.__price
#     @price.setter#p.price=2000 garna milcha
#     def price(self,price):
#         if price <= 0:
#             #return "could not set price less than zero"
#             print("could not set price less than zero8")
#             return
#         self.__price = price
# p =Product("T shirt",1000)
# print(p.name)
# print(p.__dict__)#kunai obj ko value haru herna milyo dictionary ko form ma
# p.price=2000
# p.price=-1
# print(p.price)
# print(p._Product__price)#without property and price setter
# print(p.__dict__)


#day 19

#import ways

#from oop import Product as Prod, calculate_sum
#or
#import oop as o
#or
#from oop import *(*->file ma bhayeko sabai import but not recommended as k import bhayeko thaha hundaina k use bhayeko)








