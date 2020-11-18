n=int(input()) #nº de testes
for i in range(n):
    deTroca=naoPrecisamMudar=0
    nota = []
    m=int(input()) #nº de alunos para cada teste
    notas=list(map(float, input().split()))
    for h in range(len(notas)):
        nota.append(notas[h])
    for j in range(1, len(nota)):
        for k in range(len(nota)):
            if nota[j] > nota[k]:
                deTroca = nota[k]
                nota[k] = nota[j]
                nota[j] = deTroca
    naoPrecisamMudar = len(nota)
    for l in range(len(nota)):
        if nota[l] != notas[l]:
            naoPrecisamMudar-=1
    print(int(naoPrecisamMudar))