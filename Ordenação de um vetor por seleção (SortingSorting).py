teste = list(map(int, input().split()))
def trocar(vals, posX, posY):
    vals[posX], vals[posY] = vals[posY], vals[posX]
    return None
def selecionarMenor(vals, inicio):
    localMenor = inicio
    for pos in range(inicio + 1, len(vals) ):
        if vals[pos] < vals[localMenor]:
            localMenor = pos
    return localMenor
def ordem(val):
    for i in range(len(val)-1):
        menor=selecionarMenor(val, i)
        trocar(val, i, menor)
    return None

ordem(teste)
print(teste)