n = int(input())
check = 0

for m in range(n):
    enderecos, c = [int(a) for a in input().split()]
    hash = {str(b) : [] for b in range(enderecos)}
    entrada = [int(c) for c in input().split()]
    if check:
        print()
    for i in entrada:
        resto = i % enderecos
        hash[str(resto)].append(int(i))
    for j in hash:
        print('%d -> ' % int(j), end = '')
        for k in hash[j]:
            print('%d -> ' % k, end = '')
        print('\\')
    check = 1