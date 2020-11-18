operacao=str.upper(input())
matriz=[]
soma=0
for l in range(12):
    matriz=matriz+[[0]*12]
    for c in range(0, 12):
        matriz[l][c]=float(input())
        if c > l:
            soma += matriz[l][c]
if operacao=="M":
    print("{:.1f}".format(soma/66))
if operacao=="S":
    print("{:.1f}".format(soma))