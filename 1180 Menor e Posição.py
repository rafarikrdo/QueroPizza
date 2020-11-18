N=int(input())
numeros=list(map(int, input().split()))
for i in range(0,N):
    if i == 0:
        menor=numeros[i]
        pos=i
    elif numeros[i]<menor:
        menor=numeros[i]
        pos=i
print("Menor valor: {}".format(menor))
print("Posicao: {}".format(pos))
