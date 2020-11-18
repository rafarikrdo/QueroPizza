list=[]
a=0
for i in range(20):
    n = int(input())
    list.append(n)
list.reverse()
for i in range(20):
    print("N[{}] = {}".format(i,list[i]))