n= int(input())
for i in range(n):
    primeira, segunda=map(str, input().split())
    a=b=0
    combinado = ""
    if len(primeira) <= len(segunda):
        a=len(primeira)
        b=len(segunda)
        for i in range(a):
            combinado += primeira[i]+segunda[i]
        for l in range(a, b):
            combinado += segunda[l]
    if len(primeira) > len(segunda):
        a=len(segunda)
        b=len(primeira)
        for i in range(a):
            combinado += primeira[i] + segunda[i]
        for k in range(a, b):
            combinado += primeira[k]
    print(combinado)