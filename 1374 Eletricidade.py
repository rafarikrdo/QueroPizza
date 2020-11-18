quantasMedidas = int(input())
while quantasMedidas != 0:
    datas = []
    diasPossiveis = gastoCalculado = 0
    for i in range(quantasMedidas):
        linha = input()
        dia, mes, ano, consumo = map(int, linha.split())
        datas.append([dia, mes, ano, consumo])
    for j in range(1, len(datas)):
        if datas[j][2] == datas[j-1][2]:
            if datas[j][1] == datas[j-1][1]:
                if (datas[j][0] - 1) == datas[j-1][0]:
                    diasPossiveis +=1
                    gastoCalculado += datas[j][3] - datas[j-1][3]
            if (datas[j][1] - 1) == datas[j-1][1]:
                if datas[j][0] == 1:
                    if datas[j-1][1] == 1 or datas[j-1][1] == 3 or datas[j-1][1] == 5 or datas[j-1][1] == 7 or datas[j-1][1] == 8 or datas[j-1][1] == 10:
                        if datas[j-1][0] == 31:
                            diasPossiveis += 1
                            gastoCalculado += datas[j][3] - datas[j - 1][3]
                    if datas[j-1][1] == 2:
                        if datas[j-1][0] == 29 and (datas[j-1][2] % 4) == 0 and (datas[j-1][2] % 100) != 0:
                            diasPossiveis += 1
                            gastoCalculado += datas[j][3] - datas[j - 1][3]
                        elif datas[j-1][0] == 28 and (datas[j-1][2] % 4) != 0:
                            diasPossiveis += 1
                            gastoCalculado += datas[j][3] - datas[j - 1][3]
                    if datas[j-1][1] == 4 or datas[j-1][1] == 6 or datas[j-1][1] == 9 or datas[j-1][1] == 11:
                        if datas[j-1][0] == 30:
                            diasPossiveis += 1
                            gastoCalculado += datas[j][3] - datas[j - 1][3]
        if (datas[j][2] - 1) == datas[j-1][2]:
            if datas[j-1][1] == 12 and datas[j-1][0] == 31 and datas[j][0] == 1 and datas[j][1] == 1:
                diasPossiveis += 1
                gastoCalculado += datas[j][3] - datas[j - 1][3]
    print("{} {}".format(diasPossiveis, gastoCalculado))
    quantasMedidas = int(input())