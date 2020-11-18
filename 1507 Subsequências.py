from difflib import get_close_matches
n=int(input()) #numero de testes
for i in range(n):
    s=input() #sequencia de caracteres
    q=int(input()) #numero de queries
    for j in range(q):
        r=input() #substrings a serem procuradas
        secao = s.find(r)
        if secao != -1:
            if (s[secao:secao+len(r)]) == r:
                print("Yes")
            if (s[secao:secao+len(r)]) != r:
                print("No")
        if secao == -1:
            print("No")






        '''substring = get_close_matches(s, r)
        print(get)
        maiorSubstring= substring.find_longest_match(0, len(s), 0, len(r))
        if maiorSubstring.size == 0 or maiorSubstring.size != len(r):
            print("No")
        else:
            print("Yes")
        if len(substring) > 0:
            print("Yes")
        else:
            print("No")'''