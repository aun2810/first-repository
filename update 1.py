# coverting bits into deecimal
# def ones_range(answer):
# coverting bits into deecimal
# ****************   simple just subtracting bits ***************


def valueofbits(x):
    b = len(x)
    l2 = []
    for i in range(1, b + 1):
        if x[-i] == "1":
            l2.append(-i)
    l3 = []
    for i in l2:
        b = -i
        c = b - 1
        l3.append(c)
    count = 0
    for i in l3:
        a12 = 2 ** i
        count = count + a12
    return count
# converting decimal into bits
def converting_into_decimal(a):
    l1 = []
    while (True):
        c1 = a % 2
        c2 = int(a / 2)
        a = c2
        if c1 == 0:
            l1.append('0')
        else:
            l1.append('1')
        if a == 0:
            break
    # print(l1)

    l2 = l1[::-1]
    l2.insert(0,'0')


    final_bits3="".join(l2)
    return final_bits3

def bit_seperator(a):
    a1 = list(a)
    # ['1', '2', '3', '+', '1', '2', '3']
    l1 = []
    a3 = "+-*/"
    b = 0
    for i in range(len(a1)):
        if a1[i] not in a3:
            l1.append(a1[i])
        elif a1[i] in a3:
            b = i
            break
    b1 = a1[b]

    l2 = []
    for i in range(b, len(a1)):
        if a1[i] not in a3:
            l2.append(a1[i])
    f1 = "".join(l1)
    f2 = "".join(l2)

    # f3 = int(f1)
    # f4 = int(f2)
    return f1,f2,b1
def bool1(c1):
    bit_no_1 = c1[0]
    bit_no_2 = c1[1]
    operator1 = c1[2]
    value_in_decimal1 = valueofbits(bit_no_1)
    value_in_decimal2 = valueofbits(bit_no_2)
    if operator1=='+':
        bool2=value_in_decimal1+value_in_decimal2
    else:
        bool2=value_in_decimal1-value_in_decimal2
    return bool2
def twos_calculator(l2):
    # l2 = "1010010"
    l3 = list(l2)
    l1 = []
    for i in range(1, len(l3) + 1):
        if l3[-i] == "1":
            l1.append(-i)
    a = l1[0]
    b = -a
    for i in range(b + 1, len(l3) + 1):
        if l3[-i] == "1":
            l3[-i] = "0"
        else:
            l3[-i] = "1"
    l2 ="".join(l3)
    return l2
def ones_calculator(k):
    j = list(k)
    for i in range(len(j)):
        if j[i] == "1":
            j[i] = "0"
        else:
            j[i] = "1"


    k = "".join(j)
    return k
# now taking input of a number and then calculate one's or two's

a1=str(input("enter your question \n"))
x1=str(input("you want your answer in \n"
             "1)Usingned enter (1) \n"
             "2)one's enter(2) \n"
             "3)two's enter(3)  \n"))
c=bit_seperator(a1)
d1=list(c)
# print(c1)


final_answer1=bool1(d1)
final_answe_final=converting_into_decimal(final_answer1)

if x1=="3":
    print("your answer in two's is ",twos_calculator(final_answe_final))
elif x1=="2":
    print("your answer in one's is ",ones_calculator(final_answe_final))
elif x1=="1":
    print(final_answe_final)
else:
    print("give a valid input ")