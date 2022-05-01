class kum:
    def execute(self):
        print("ahjdsdkasd")
class aun:
    def hello(self,name):
        name.execute()
        # name.execute()


obj=kum()

ayez1 = aun()
ayez1.hello(obj)


# class normal_calc:
#     def __init__(self,no1,no2):
#         self.no1=no1
#         self.no2=no2
#     # def operator_entrormal_calc.display()
#     #         normal_calc2.display()y(self):
#     #     self.operator=input("enter operator")
#     def display(self):
#         print("the answer is ",self.no1+self.no2)
#         print("the answer is ", self.no1 - self.no2)
# class normal_calc2:
#     def display1(self):
#         print("the answer is ", self.no1 * self.no2)
#         print("the answer is ", self.no1 / self.no2)
#
# class hybrid(normal_calc,normal_calc2):
#     pass
#     # def display(self):
#     #     n
# obj=hybrid(2,3)
# obj.display()
# obj.display1()






# class bank_account:
#     def __init__(self,name,acc_no,balance=0):
#         self.name=name
#         self.acc_no=acc_no
#         self.balance=balance
#         # self.balance=0
#     def deposit(self):
#         self.dep=int(input("enter the amount you wanted to deposit \n"))
#         self.balance=self.balance+self.dep
#         return self.balance
#     def widthdrwal(self):
#         self.width=int(input("enter the amount you wanted to widthdraw \n"))
#         self.balance=self.balance-self.width
#         return self.balance
#     def bank_fees(self):
#         self.balance=self.balance-(self.balance*0.05)
#         return self.balance
#     def display(self):
#         print("the remaing account balance is {}".format(self.balance))
# l1=['deposit','widthdrwal','bank_fees','display']
#
# obj=bank_account("syed aun muhammad ",1234324,100)
# obj.deposit()
# obj.widthdrwal()
# obj.bank_fees()
# obj.display()







# class rectangle:
#     def __init__(self,x,y):
#         self.height=x
#         self.width=y
#     def area(self):
#         self.area_of_rec=self.height*self.width
#         return self.area_of_rec
#     def perimeter(self):
#         self.per=2*self.height*self.width
#         return self.per
#     def display(self):
#         print("the area is {} and the perimeter is {}".format(self.area_of_rec,self.per))
# class paralelopie(rectangle):
#     animal="adan"
#
#     def __init__(self,x,y,z):
#         super(paralelopie,self).__init__(x,y)
#         self.hell=z
#     def volume(self):
#         self.vol=3*self.height*self.width
#         return self.vol
#     def display(self):
#         print("the area is {} and the perimeter is {} and the volume is {}" .format(self.area_of_rec,self.per,self.vol))
#         print(self.hell)
# obj=paralelopie(12,3,4)
# obj.area()
# obj.perimeter()
# obj.volume()
# obj.display()


# class aun:
#     a=12
#     def __init__(self):
#         c=0
#         self.a=21
#         self.b=22
#     def add(self):
#         self.c=self.a+self.b
#         return self.c
#     def display(self):
#         print("the sum of the numbers is ",self.c)
#     # def hello1(self):
#     #     print("hello")
# aun_obj=aun()
# aun_obj.add()
# aun_obj.display()