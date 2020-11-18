quantosTamanhos = int(input())
while quantosTamanhos != 0:
    conjuntos = []
    retangulos = varetas = 0
    for i in range(quantosTamanhos):
        linha = input()
        tamanho, quantidade = map(int, linha.split())
        conjuntos.append([tamanho, quantidade])
    if quantosTamanhos == 1:
        retangulos = quantidade//4
    else:
        for j in range(0, len(conjuntos)):
            while conjuntos[j][1] >= 2:
                conjuntos[j][1] = conjuntos[j][1] - 2
                varetas += 2
        retangulos = varetas // 4
    print(retangulos)
    quantosTamanhos = int(input())