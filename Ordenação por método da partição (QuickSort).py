def trocar(vals, posX, posY):
    vals[posX], vals[posY] = vals[posY], vals[posX]
    return None
def particiona(vals, inicio, fim):
    pivo = vals[inicio]
    i = inicio + 1
    j = fim
    while i < j:
        while i < fim and vals[i] < pivo:
            i +=1
        while j > inicio and vals[j] >= pivo:
            j -= 1
        if i < j:
            trocar(vals, i, j)
    if pivo>vals[j]:
        trocar(vals, inicio,j)
    return j
def quickSort(vals, inicio, fim):
    if inicio < fim:
        posPivo=particiona(vals, inicio, fim)
        quickSort(vals, inicio, posPivo-1)
        quickSort(vals, posPivo+1, fim)
    return None
def ordena(valores):
    quickSort(valores, 0, len(valores)-1)
    return None