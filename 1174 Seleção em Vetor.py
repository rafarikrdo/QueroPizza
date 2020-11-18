list=[]
for i in range(100):
    n=float(input())
    list.append(n)
    if n<=10:
        print("A[{}] = {:.1f}".format(i, list[i]))
