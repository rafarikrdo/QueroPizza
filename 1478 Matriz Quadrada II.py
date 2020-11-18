valores=[]
quad = int(input())
while quad != 0:
    valores=[[0 for i in range(quad)] for i in range (quad)]
    for i in range(quad):
        for j in range(quad):
            if i == j:
                valores[i][j] = 1
            else:
                if i > j:
                    valores[i][j] = (i + 1) - j
                elif j>i:
                    valores[i][j] = j + 1 - i
    for lin in range(len(valores)):
        for col in range(len(valores[lin])):
            if col != len(valores[lin]) - 1:
                print("%3d" % valores[lin][col], end=" ")
            if col==len(valores[lin]) - 1:
                print("%3d" % valores[lin][col], end="")
        print()
    print("")
    quad=int(input())