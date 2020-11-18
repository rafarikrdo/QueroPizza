n=int(input()) #numero de testes
#cada teste, uma linha
vezes=maiorNdeVezes=0
maisFrequente = final = ""
aLista=[]
for i in range(n):
    entrada=input()
    avaliada=entrada.lower()
    linha=list(map(str, avaliada))
    for j in range(len(linha)):  #para todo caracter
        if linha[j] != " ":
            vezes=linha.count(linha[j])
            if vezes == maiorNdeVezes:
                aLista.append(linha[j])
            if vezes > maiorNdeVezes:
                aLista = [linha[j]]
                maiorNdeVezes = vezes
    for l in range(len(aLista)):
        if aLista.count(aLista[l]) > 1:
            aLista = [aLista[l]]
        if l == " ":
            del aLista[l]
        print(aLista)

    maisFrequente = ""
    aLista=[]
vezes=maiorNdeVezes=0