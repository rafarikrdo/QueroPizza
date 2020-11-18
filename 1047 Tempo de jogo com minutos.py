a, b, x, y=map(int, input().split())
hrs=min=0
if y>b:
    min=y-b
    if x > a:
        hrs = x - a
    elif x==a:
        hrs=0
    elif a>x:
        hrs = 24 - (a-x)
elif b>y:
    min=60-(b-y)
    if x > a:
        hrs = x - a - 1
    elif x==a:
        hrs=23
    elif a > x:
        hrs = 23 - (a-x)
elif b==y:
    if x > a:
        hrs = x - a
    elif x < a:
        hrs = 24 - (a - x)
    elif x==a:
        hrs=24
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hrs, min))