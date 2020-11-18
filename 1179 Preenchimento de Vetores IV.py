par=[]
impar=[]
for i in range(15):
    num=int(input())
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
    if len(impar) == 5:
        for j in range(0,5):
            print("impar[{}] = {}".format(j, impar[j]))
        impar=[]
    if len(par) == 5:
        for k in range(0,5):
            print("par[{}] = {}".format(k, par[k]))
        par=[]
for l in range(0, len(impar)):
    print("impar[{}] = {}".format(l, impar[l]))
for m in range(0, len(par)):
    print("par[{}] = {}".format(m, par[m]))
print(impar, par)