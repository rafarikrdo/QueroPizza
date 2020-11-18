notas=soma=0
while notas<2:
    n=float(input())
    if n>=0 and n<=10:
        soma = soma + n
        media=soma/2
        notas+=1
    else:
        print("nota invalida")
print("media = {:.2f}".format(media))