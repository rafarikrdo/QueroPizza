'''
Faça um editor de arquivos texto, com operações:
(1) Mostrar Arquivo
(2) Inserir Linha em Arquivo
(3) Remover Linha de Arquivo
(4) Copiar Arquivo
(5) Apagar Arquivo
(6) Criar Arquivo Vazio
(7) Sair do Editor


Restrição: Está proibido manter todo o conteudo do arquivo
em memória principal

'''
# Subs
def menu():
    print("Menu de Opções:")
    print("(1) Mostrar Arquivo")
    print("(2) Inserir Nova Linha")
    print("(3) Remover Linha")
    print("(4) Copiar Arquivo")
    print("(5) Apagar Aquivo")
    print("(6) Criar Aquivo Vazio")
    print("(7) Sair do Editor")
    escolha = int(input("Sua Escolha: "))
    return escolha

def mostrar(nm):
    dados = open(nm, "r", encoding="utf-8")
    print("Conteúdo do Arquivo", nm+":")
    for linha in dados:
        print(linha.strip("\n"))
    print()
    dados.close()
    return None

def criar(nm):
    dados = open(nm, "w")
    dados.close()
    return None

def inserir(nm, nova, pos):
    import os
    dados = open(nm, "r", encoding="utf-8")
    dadosAux = open("temporario", "w", encoding="utf-8")
    for linha in dados:
        if pos == 1:
            dadosAux.write(nova+"\n")
        dadosAux.write(linha)
        pos -= 1
    if pos >= 1:
        dadosAux.write(nova+"\n")
    dadosAux.close()
    dados.close()
    os.remove(nm)
    os.rename("temporario", nm)
    return None

def remover(nm, pos):
    import os
    dados = open(nm, "r", encoding="utf-8")
    dadosAux = open("temporario","w", encoding="utf-8")
    for linha in dados:
        if pos != 1:
            dadosAux.write(linha)
        pos -= 1
    dadosAux.close()
    dados.close()
    os.remove(nm)
    os.rename("temporario", nm)
    return None

def apagar(nm):
    import os
    os.remove(nm)
    return None

def copiar(nm, mnCopia):
    dados = open(nm, "r", encoding="utf-8")
    dadosCopia = open(mnCopia, "w", encoding="utf-8")
    for linha in dados:
        dadosCopia.write(linha)
    dadosCopia.close()
    dados.close()
    return None

def processa(op):
    if op == 1:
        nomeArq = input("Nome do Arquivo a ser Mostrado: ")
        mostrar(nomeArq)
    elif op == 2:
        nomeArq = input("Nome do Arquivo a ser Modificado: ")
        novaLinha = input("Diga o conteúdo da nova linha a ser inserida: ")
        posicao = int(input("Diga o posicionamento da linha nova: "))
        inserir(nomeArq, novaLinha, posicao)
    elif op == 3:
        nomeArq = input("Nome do Arquivo a ser Modificado: ")
        posicao = int(input("Diga o posicionamento da linha a ser removida: "))
        remover(nomeArq, posicao)
    elif op == 4:
        nomeArq = input("Nome do Arquivo a ser Copiado: ")
        nomeArqCopia = input("Nome do Arquivo para onde será Copiado: ")
        copiar(nomeArq, nomeArqCopia)
    elif op == 5:
        nomeArq = input("Nome do Arquivo a ser Eliminado: ")
        apagar(nomeArq)
    elif op == 6:
        nomeArq = input("Nome do Arquivo a ser Criado Vazio: ")
        criar(nomeArq)
    return None

# PP
opcao = menu()
while opcao != 7:
    processa(opcao)
    opcao = menu()
print("Obrigado por usar nosso editor!!!")