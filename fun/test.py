def  getFirst(num):
    s = str(num)[0]
    return int(s)

def getEnd(num):
    s = str(num)
    s = s[len(s)-1]
    return int(s)

for i in range(10,99):
    a = getFirst(i)
    b = getEnd(i)
    c = pow(i,3)
    a_1 = getFirst(c)
    b_1 = getEnd(c)
    if a == a_1 and b == b_1:
        print(i,a,b,c)



