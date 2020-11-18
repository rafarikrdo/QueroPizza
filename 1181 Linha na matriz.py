n=int(input())
operacao=str.upper(input())
matriz=[]
soma=0
for l in range(12):
    matriz=matriz+[[0]*12]
    for c in range(0, 12):
        matriz[l][c]=float(input())
for i in range(12):
    soma += matriz[n][i]
if operacao=="M":
    print("{:.1f}".format(soma/12))
if operacao=="S":
    print("{:.1f}".format(soma))