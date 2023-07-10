#day 18

#1.
# try:
#     a=int(input("enter any number:"))
#     b=int(input("enter another number:"))
#     print(a+b)
# except ValueError:
#     print("Only interger is accepted")


# name=input("enter name:")
# print(name)


#a b ma string halyo bhane error aucha ani euta problem le program nai run bhayena
#mostly user or internal reseon or data dherai bhayo or list read garda garadai root nai sakyo,etc
#kunai thau ma exception auna sakcha jasto lagyo bhane throw garera catch garna parcha

# syntax:
#try:
    # block of code
# except Exception:
#     handle
# except Exception:
#     handle
# else:
#     only execute when try succeed
# finally:
#     execute no matter what

#2.
# a=[1,2,3,4]
# try:
#     print(a[4])
# except IndexError:
#     print("data not found")

#3.to not stop even if there is value error
while True:
    try:
        a=int(input("enter any number:"))
        b=int(input("enter another number:"))
        print(f"sum is {a+b}")
        break
    except ValueError:
        print("Only interger is accepted")
        continue

#4.
class ProductPriceError(Exception):
    pass
class Product:
    def __init__(self,name,price):
        self.name = name
        self.__price = price
        #_=protected
        #__=private
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        if price <= 0:
            raise ProductPriceError("could not set price less than zero8")
        self.__price = price
if __name__=="main":
    p =Product("T shirt",1000)
    print(p.name)
    print(p.__dict__)
    try:
        p.price = -1
    except ProductPriceError as err:#err or msg
        print(err)
    print(p.__dict__)

        




















