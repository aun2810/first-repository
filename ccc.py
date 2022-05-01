# f=open("aun1.txt","a")
# f.write("hello\n")
# f.write("hell\n")
# f.close()
f=open("aun1.txt","r")
c=f.readlines()
f.close()
d1='hello1'
print(d1 in c)
