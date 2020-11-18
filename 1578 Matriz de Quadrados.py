quantasMatrizes = int(input())
for i in range(quantasMatrizes):
    ordem = int(input())
    matriz = [[1 for p in range(ordem)]for l in range(ordem)]
    matrizQuadrada = [[1 for mc in range(ordem)]for rr in range(ordem)]
    for j in range(ordem):
        matriz[j] = list(map(int, input().split()))
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            a = matriz[linha][coluna]
            matrizQuadrada[linha][coluna] = a ** 2

    maiores = []
    for col in range(ordem):
        maior = 0
        for lin in range(ordem):
            if matrizQuadrada[lin][col] > maior:
                maior = matrizQuadrada[lin][col]
        maior = str(maior)
        maiores.append(len(maior))

    for col in range(ordem):
        for lin in range(ordem):
            valores = len(str(matrizQuadrada[lin][col]))
            espacos = maiores[col] - valores
            matrizQuadrada[lin][col] = str(" " * espacos) + str(matrizQuadrada[lin][col])

    c = 4+i
    print("Quadrado da matriz #{}:".format(c))
    for x in range(0, ordem):
        for y in range(0, ordem - 1):
            print(matrizQuadrada[x][y], end=" ")
        print(matrizQuadrada[x][ordem - 1])
    c = 4+i

    if i != quantasMatrizes - 1:
        print("")