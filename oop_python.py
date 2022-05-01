# ******** duck typing *******



#  ************ inheritance**********
# point #1
#  as the constructors in c++ automatically run in oop but in python the constructor
#  of base class only run when you write this command(super()._init_()
# point #2
# in multiple inheritance if two class have the functions with the same name then whom function will call first (A,B)
# which is define first such as a above
# point #3
# you can also use the base function and name them according to you in dervied class
# class A:
#     def __init__(self):
#         print("hello i am const 1")
#     def func(self):
#         print('i am func of class A')
#     def hello(self):
#         print("hello world")
# class B:
#     def __init__(self):
#         print("hello i am const 2")
#     def func(self):
#         print("i am fun of class B")
#
# # single level
# # class C(A):
# #     def __init__(self):
# #         print("hello i am const 3")
# # multple inheritance(example of point 2)
# class C(A,B):
#     def __init__(self):
#         # example of point #1
#         super().__init__()
#         print("hello i am const 3")
#     # example of point #3
#
#     def hello1(self):
#         super().hello()
#
# obj1=C()
# obj1.hello1()
# obj1.func()



# class A():
#     pass
# class B():
#     pass
#
# class C(A):
# class C(A,B):
#     pass



# ****************** inner class in python******
# class student:
#     def __init__(self, name, clas):
#         self.name=name
#         self.clas=clas
#         # there is class within a class so here we are creating object of the inner class that contain all the attributes of second class
#         self.lap=self.laptop()
#     def show(self):
#         print(self.name,self.clas)
#         self.lap.show()
#     class laptop:
#         def __init__(self):
#             self.brand="hp"
#             self.ram="4gb"
#         def show(self):
#             print(self.brand,self.ram)
#
# obj1=student("aun","2smes")
# obj1.show()

# creating object to an obect
# obj1_1=obj1.lap
#another method
# accessing values of object and object like this
# print(obj1.lap.brand)
# print(obj1.lap)











# class method
# class student:
#     school="NASRA SCHOOL"
#
#     def __init__(self,name,clas):
#         self.name=name
#         self.clas=clas
#     @classmethod
#     def school_info(cls):
#         return cls.school
#
# obj1=student("syed aun","2semester")
# print(obj1.school_info())
