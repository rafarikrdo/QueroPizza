n=int(input())
for i in range(n):
    linha = input()
    led = 0
    for l in range(len(linha)):
        if linha[l] == '0' or linha[l] == '9' or linha[l] == '6':
            led += 6
        if linha[l] == '1':
            led += 2
        if linha[l] == '2' or linha[l] == '3' or linha[l] == '5':
            led += 5
        if linha[l] == '4':
            led += 4
        if linha[l] == '7':
            led += 3
        if linha[l] == '8':
            led += 7
    print(led, "leds")