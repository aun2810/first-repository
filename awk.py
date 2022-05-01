


# a1=str(input("enter"))
# print(a1)
a=str(input("enter"))
a1=list(a)
# ['1', '2', '3', '+', '1', '2', '3']
l1=[]
a3="+-*/"
b=0
for i in range(len(a1)):
    if a1[i] not in a3:
        l1.append(a1[i])
    elif a1[i] in a3:
        b=i
        break
b1=a1[b]
l2=[]
for i in range(b,len(a1)):
    if a1[i] not in a3:
        l2.append(a1[i])
f1="".join(l1)
f2="".join(l2)
f3=int(f1)
f4=int(f2)
if b1=="+":
    print(f3+f4)
elif b1=="-":
    print(f3-f4)
elif b1=="*":
    print(f3*f4)
elif b1=="/":
    print(f3/f4)
else:
    print("good bye ")