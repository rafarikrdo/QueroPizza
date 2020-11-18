n=int(input())
list=[]
list.append(n)
for i in range(1,10):
    obj=n*(2**i)
    list.append(obj)
for i in range(10):
    print("N[{}] = {}".format(i,list[i]))