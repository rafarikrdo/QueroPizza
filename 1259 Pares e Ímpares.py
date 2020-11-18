n=int(input()) #Número de entradas
par=[]
impar=[]
for i in range(n):
    valor=int(input())
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 != 0:
        impar.append(valor)
paresOrdenados = sorted(par)
imparesOrdenados=reversed(sorted(impar))
'''for j in range(1, len(par)):
    for k in range(len(par)):
        deTroca=0
        if par[j] < par[k]:
            deTroca = par[k]
            par[k] = par[j]
            par[j] = deTroca
for j in range(1, len(impar)):
    for k in range(len(impar)):
        deTrocx=0
        if -impar[j] > impar[k]:
            deTrocx = impar[k]
            impar[k] = impar[j]
            impar[j] = deTrocx'''
for val in paresOrdenados:
    print(val)
for ores in imparesOrdenados:
    print(ores)
