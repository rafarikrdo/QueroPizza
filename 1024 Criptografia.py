from math import ceil

n = int(input())
for i in range(n):
    linha = str(input())
    linhx = ''
    for x in linha:
        if (x.isalpha() == True):
            linhx += chr(ord(x) + 3)
        else:
            linhx += x
    linhy = linhx[::-1]
    inteiro = ceil(len(linhy)/2)
    linhz = linhy[-inteiro:]
    linhw = ''
    for y in linhz:
        linhw += chr(ord(y) - 1)
    mensagemFinal = linhy.replace(linhz, linhw)
    print(mensagemFinal)