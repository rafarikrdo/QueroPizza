entradas = int(input())
for j in range(entradas):
    linhas, colunas = map(int, input().split())
    sonares = (linhas//3)*(colunas//3)
    print(sonares)