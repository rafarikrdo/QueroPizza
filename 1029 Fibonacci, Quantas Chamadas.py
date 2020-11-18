chamadas = [1, 1]
fib= [0, 1]
for i in range(2, 40):
    chamadas.append(chamadas[i - 1] + chamadas[i - 2] + 1)
    fib.append(fib[i - 1] + fib[i - 2])

vezes = int(input())
for j in range(vezes):
    n = int(input())
    print("fib({}) = {} calls = {}".format(n, chamadas[n] - 1, fib[n]))