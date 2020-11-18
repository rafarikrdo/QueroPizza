Fib=[0,1]
seguinte=0
a=0
vezes=int(input())
for i in range(vezes):
    N=int(input())
    while len(Fib) <= N:
        seguinte=Fib[a]+Fib[a+1]
        a+=1
        Fib.append(seguinte)
    print("Fib({}) = {}".format(N, Fib[N]))
print(Fib)