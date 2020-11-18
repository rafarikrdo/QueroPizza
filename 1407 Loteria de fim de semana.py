linha = input()
while linha != "0 0 0":
    sorteios, numerosNaAposta, valorMaximo = map(int, linha.split())
    tentativa = []
    minOcorrencia = []
    todosEscolhidos = []
    menorOcorrencia = sorteios*numerosNaAposta + 1
    for i in range(sorteios):
        tentativa.append(list(map(int, input().split())))
    for j in range(sorteios):
        for k in range(numerosNaAposta):
            todosEscolhidos.append(tentativa[j][k])
    for ss in range(1, valorMaximo+1):
        if todosEscolhidos.count(ss) == menorOcorrencia:
            minOcorrencia.append(ss)
        if todosEscolhidos.count(ss) < menorOcorrencia:
            minOcorrencia = [ss]
            menorOcorrencia = todosEscolhidos.count(ss)
    for val in range(len(minOcorrencia)):
        if val == 0:
            aImprimir = str(minOcorrencia[0])
        else:
            aImprimir += " " + str(minOcorrencia[val])
    print(aImprimir)
    linha = input() 