n = int(input())
for i in range(n):
    linha = input().split()
    linha.sort(key=len, reverse=True)
    for i in range(len(linha)):
        print(linha[i], end = '')
        if i != len(linha)-1:
            print(' ', end = '')
    print()