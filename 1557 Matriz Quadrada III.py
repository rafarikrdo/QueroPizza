ordem=int(input())
matriz=[]
while ordem != 0:
    matriz = [[1 for j in range(ordem)] for l in range(ordem)]
    for i in range(1, ordem):
        matriz[0][0]=1
        matriz[0][i]=matriz[0][i-1]*2
        matriz[i][0]=matriz[0][i]
        for j in range(1, ordem):
            matriz[i][j]=matriz[i][j-1]*2
    if ordem <=2:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%1d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%1d" % matriz[lin][col], end="")
            print()
        print("")
    elif 3 <= ordem <= 4:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%2d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%2d" % matriz[lin][col], end="")
            print()
        print("")
    elif ordem == 5:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%3d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%3d" % matriz[lin][col], end="")
            print()
        print("")
    elif 6<=ordem<=7:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%4d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%4d" % matriz[lin][col], end="")
            print()
        print("")
    elif 8<=ordem<=9:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%5d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%5d" % matriz[lin][col], end="")
            print()
        print("")
    elif ordem == 10:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%6d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%6d" % matriz[lin][col], end="")
            print()
        print("")
    elif ordem == 11 or ordem == 12:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%7d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%7d" % matriz[lin][col], end="")
            print()
        print("")
    elif 13<=ordem<=14:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%8d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%8d" % matriz[lin][col], end="")
            print()
        print("")
    elif ordem == 15:
        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if col != len(matriz[lin]) - 1:
                    print("%9d" % matriz[lin][col], end=" ")
                if col == len(matriz[lin]) - 1:
                    print("%9d" % matriz[lin][col], end="")
            print()
        print("")
    ordem = int(input())