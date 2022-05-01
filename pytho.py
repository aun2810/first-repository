d1={"bread":{"prize":70,"quantity":10},
    "butter":{"prize":100,"quantity":20},
    "milk":{"prize":110,"quantity":23},
    "coffee":{"prize":1000,"quantity":30}}
l1=[]
l2=[]
l3=[]
l4=[]

print("items we have ")
for i in d1.keys():
    l1.append(i)
for i in d1.values():
    l2.append(i)
for i in range(len(l1)):
    print(i+1,")",l1[i])
for i in l1:
    l3.append(d1[i]["prize"])
l5=[]
i1=int(input("enter how many items you wana buy "))
i=0
while(i<=i1):
    # a=str(input("do you wana buy something   \n"))
    # if a=="yes":
    a2=str(input("enter name of an item"))
    a3=int(input("enter the no of "))
    l4.append(a2)
    if a3==1:
        l5.append(d1[a2]["prize"])
    else:
        a=a3*d1[a2]["prize"]
        l5.append(a)
        a4=d1[a2]["quantity"]
        d1[a2]["quantity"]=a4-a3
    i=i+1

print("the items you bought is \t\t\t prize")
for i in range(len(l4)):
    print(i+1,l4[i],"\t\t\t\t\t\t\t",l5[i])
print("your total bill is ",sum(l5))
for i in d1.keys():
    print("the items left",i,d1[i]["quantity"])
# in_put=str(input("enter the items you wana buy"))
