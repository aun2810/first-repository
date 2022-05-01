l1=[2,4,1,5]
for i in range(len(l1)):
    for j in range(0,(len(l1)-1)-i):

        if l1[j]>l1[j+1]:
            temp = l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
print(l1)
# import mysql.connector
# mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810",database="sql_hr")
# mycur=mydb.cursor()
# mycur.execute("select * from employees")
# for i in mycur:
#     print(i)


# print(mydb)
# if (mydb):
#     print("hello")
# else:
#     print("sorry")

# *************little project******
# coverting bits into deecimal
# def valueofbits(x):
#     b = len(x)
#     l2 = []
#     for i in range(1, b + 1):
#         if x[-i] == "1":
#             l2.append(-i)
#     l3 = []
#     for i in l2:
#         b = -i
#         c = b - 1
#         l3.append(c)
#     count = 0
#     for i in l3:
#         a12 = 2 ** i
#         count = count + a12
#     return count
#
#
#
#
# a=str(input("enter a binary number \n"))
# b=str(input("enter a binary number \n"))
# print("the answer of ",a,valueofbits(a))
# print("the answer of ",b,valueofbits(b))
# valueofbits(b)









# # method to find the integer no of bit that is represented here
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







# finding negative sign range
a=int(input("enter a number "))
n=0
b=1
while(True):
    a2=(2**(n-1))-1
    a1=-a2
    if a>a1:
        b=n
        break
    n+=1
print(b)
#method to calculate signed bits if no is positive
a=18
n=0
b=1
while(True):
    a1=(2**(n-1))-1
    if a<a1:
        b=n
        break
    n+=1
print(b)

#
#
#
# #method to calculate unsigned bits
# a=18
# n=0
# b=1
# while(True):
#     a1=2**n
#     if a<a1:
#         b=n
#         break
#     n+=1
# print(b)




# def aunali(l2):
#     # l2 = "1010010"
#     l3 = list(l2)
#     l1 = []
#     for i in range(1, len(l3) + 1):
#         if l3[-i] == "1":
#             l1.append(-i)
#     a = l1[0]
#     b = -a
#     for i in range(b + 1, len(l3) + 1):
#         if l3[-i] == "1":
#             l3[-i] = "0"
#         else:
#             l3[-i] = "1"
#     l2 = "".join(l3)
#     print(l2)
#
#
# k = str(input("enter a binary number  \n"))
# j=list(k)
# for i in range(len(j)):
#     if j[i]=="1":
#         j[i]="0"
#     else:
#         j[i]="1"
# aunali(k)
#
# k="".join(j)
# print("the one's compliment of a number is \n",k)


# def ones():
#     for j in i:
#         print(j)
#
# # hel="12313"
# i=str(input("enter a binary number  \n"))
# # # hel="12313"
# ones()



# def aun(n):
#     if n<2:
#         return n
#     else:
#         return aun(n-1)+aun(n-2)
# n1=10
#
# print(aun(n1))


