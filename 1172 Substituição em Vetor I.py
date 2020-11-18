list=[]
for i in range(0,10):
    n=int(input())
    if n <= 0:
        n=1
    list.append(n)
for i in range(0,10):
    print("x[{}]={}".format(i,list[i]))