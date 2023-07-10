#day 17

# class A:#parent class
#     pass
# class B(A):#child class
#     pass

#kunai pani child le kunai pani parent ko property use garna milne ani sabai kura use garna milcha
#"IS A" relationship sarisfy hunna parcha (hunnai parne chai haina)
#sub class "IS A" super class => satisfy hunna parcha eg DOG IS A ANIMAL

#1.here "IS A" condition is satisfied 
#class Parent is not possible
# class Animal:#parent class
#     pass
# class Dog(Animal):#child class
#     pass

#2.
class User:
    def __init__(self, _id, username, password):
        self._id = _id
        self.username = username
        self.password = password
    def login(self, uname, pwd)->None:#leii return gardaina bhane none return garcha
        if uname == self.username and pwd == self.password:
            print("Logged in successfully")

class Person(User):
    def __init__(self, _id, username, password, name, address):
        super().__init__(_id, username, password) #Person.__init__(self,_id, username, password, name, address)
        self.name = name
        self.address = address
    
    def __str__(self):#obj ko representation ,string representation
        return self.name#return f"{self.name} and {Self.address}."
    
    def __repr__(self):#list 
        return self.name

class Teacher(Person):
    def __init__(self, _id, username, password, name, address, designation):
        super().__init__(_id, username, password, name, address)
        self.designation = designation

class Student(Person):
    def __init__(self, _id, username, password, name, address, roll):
        super().__init__(_id, username, password, name, address)
        self.roll = roll

# u=User(10,"ram","aalu")        
# u.login("ram","aalu")
# t=Teacher(10,"ram","aalu","ram","ktm","professor")
# t.login("ram","aalu")
# s=Student(10,"cimrika","1234","cimrika","gabahal","24")
# s.login("cimrika","12345")
# print([s])
# print(s)

#3.#operator overloading
# class Product:
#     def __init__(self,name,price) :
#         self.name = name
#         self.price = price

#     def __eq__(self, __value):
#         return self.price == __value.price
    
#     def __gt__(self, __value):
#         return self.price > __value.price
    
# p1=Product("jacket",1950)
# p2=Product("laptop",2000)
# print(p1 > p2)#p1 goes to self and p2 goes to __value
# print (p1 == p2)
    







