def trocar(vals, posX, posY):
    vals[posX], vals[posY] = vals[posY], vals[posX]
    return None
def ordem(vals): #bolha correndo toda lista
    for tam in range(len(vals)-1,0,-1):
        for i in range(tam):
            if vals[i]>vals[i+1]:
                trocar(vals, i, i+1)
    return None
lista = list(map(int, input().split()))
ordem(lista)
print(lista)