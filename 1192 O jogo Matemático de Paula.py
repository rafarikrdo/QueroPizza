def digitosAndLetras(teste):
    he, she = int(teste[0]), int(teste[2])
    it = teste[1]
    if he == she:
        print(he*she)
    elif it.isupper():
        print(she - he)
    else:
        print(she + he)
    return None

vezes = int(input()) #numero de entradas
for i in range(vezes):
    linha = input()
    digitosAndLetras(linha)
