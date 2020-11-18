linha=input()
mudança = 0
posInicial = []
objetivo = []
conferir = []
while linha != "* *":
    inicial, obj = map(str, linha.split())
    inicial.upper()
    obj.upper()
    if len(inicial) == len(obj) and inicial[0] == 'B' or inicial[0] == 'N':
        for i in range(len(inicial)):
            posInicial.append(inicial[i])
            objetivo.append(obj[i])
        for j in range(len(objetivo)):
            while posInicial [j] != objetivo [j]:
                conferir.append(posInicial[j])
                a = len(conferir)
                posInicial[j] = objetivo [j]
        mudança = len(objetivo) - len(conferir)
        if a == len(objetivo):
            mudança = 1
        if inicial == obj:
            mudança = 0
        print(mudança)
        posInicial = []
        objetivo = []
        conferir= []
        mudança = 0
        linha = input()
    else:
        None
if linha == "* *":
    None