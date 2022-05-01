import mysql.connector
mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810",database="aundb1")
mycur=mydb.cursor()
# mycur.execute("select first_name,last_name from employee")
# mycur.execute("alter table employee add column religion varchar(200)" )
# mycur.execute("Select * from employee")
mycur.execute("insert into emp0(empid,na_me) values(3,'aun')")
mydb.commit()
# print(mycur)
for i in mycur:


    print(i)




# **************** calling data from two tables from my sql
# import mysql.connector
# mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810",database="aundb1")
# mycur=mydb.cursor()
# mycur.execute("select * from employee, pak")
# for i in mycur:
#     print(i)
#***************** insert statement
# # just remain one thing in mind when you are commit your connection
# import mysql.connector
# mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810",database="aundb1")
#
# mycur=mydb.cursor()
# sql="INSERT INTO pak (first_name,last_name,age) VALUES ('nisa','zehra','12')"
# mycur.execute(sql)
# mydb.commit()
# print("hello")
# for i in mycur:
#     print(i)

#******************** to call one raw from data basae


# mycur.execute("select * from customers where first_name='Babara'" )


# mycur.execute("select * from customers where customer_id=1" )

# calling only two colmns


# mycur.execute("select customer_id, first_name from customers" )


# to call a particular column only

# mycur.execute("select customer_id from customers" )

#to view all records
# mycur.execute("select * from customers")
# for i in mycur:
#     print(i)
# https://www.w3schools.com/python/python_mysql_orderby.asp (this is the link from which you can manioulate your data base)

# import mysql.connector
# mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810",database="aundb1")
# mycur=mydb.cursor()
#
# # val = ("John1", "Highway 22","22")
# # sql = "INSERT INTO pak (first_name, last_name) VALUES ('juna','hassan',22)"
# sql="INSERT INTO `aundb1`.`pak` (`first_name`, `last_name`, `age`) VALUES ( 'azan', 'haider', '121')"
# mycur.execute(sql)
#
# mydb.commit()
# print("data")

#putting data into data base
# import mysql.connector
# mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810",database="aundb1")
# mycur=mydb.cursor()
#
# # val = ("John1", "Highway 22","22")
# # sql = "INSERT INTO pak (first_name, last_name) VALUES ('juna','hassan',22)"
# sql="INSERT INTO `aundb1`.`employee` (`empid`, `first_name`, `last_name`, `age`, `dept`) VALUES ('5', 'zaran1', 'haider1', '121', '1nasra')"
# mycur.execute(sql)
#
# mydb.commit()
# print("data")
# # mycur.execute("select * from employee")
# for i in mycur:
#     print(i)


# import mysql.connector
# mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810",database="aundb1")
# mycur=mydb.cursor()
# sql="INSERT INTO customers (empid,first_name,last_name,age,dept) VALUES (%d, %s, %s, %d,%s)"
# val=(5,"John", "smith",25,"bba")
# mycur.execute(sql,val)
#
# mydb.commit()
# print("data succesfull added")
# # print("record is succesfully added ")
# # mycur.execute("SELECT * FROM aundb1.employee")
# # for i in mycur:
# #     print(i)
# # # print(mycur)




# getting data from data base
# import mysql.connector
# mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810")
# mycur=mydb.cursor()
# mycur.execute("INSERT INTO `aundb1`.`employee` (`empid`, `first_name`, `last_name`, `age`) VALUES ('5', 'jamal', 'hussain', ’19','mdcat');")
    # print("record is succesfully added ")
# mycur.execute("SELECT * FROM aundb1.employee")
# for i in mycur:
#     print(i)
# # print(mycur)










# def hello():
#     return 2+3
# def hello1():
#     c=hello()+3
#     return c
# print(hello1())




# converting decimal into bits
# def converting_into_decimal(a):
#     l1 = []
#     while (True):
#         c1 = a % 2
#         c2 = int(a / 2)
#         a = c2
#         if c1 == 0:
#             l1.append('0')
#         else:
#             l1.append('1')
#         if a == 0:
#             break
#     # print(l1)
#
#     l2 = l1[::-1]
#     l2.insert(0,'0')
#
#
#     final_bits3="".join(l2)
#     return final_bits3
#
# a1=int(input("enter a decimal number to convert it into binary \n"))
# print(converting_into_decimal(a1))














# a=str(input("enter a binary number \n"))
# b=len(a)
# l2=[]
# for i in range(1,b+1):
#     if a[-i]=="1":
#         l2.append(-i)
# l3=[]
# for i in l2:
#     b=-i
#     c=b-1
#     l3.append(c)
# count=0
# for i in l3:
#     a12=2**i
#     count=count+a12
# print(count)
