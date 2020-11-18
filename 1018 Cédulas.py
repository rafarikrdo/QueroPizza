v=int(input())
w=v
cem=cinq=vint=dez=cinc=dois=um=0
while v >= 100:
    cem += 1
    v = v-100
while v>= 50:
    cinq += 1
    v -=50
while v>=20:
    vint+=1
    v -= 20
while v >= 10:
    dez += 1
    v-=10
while v>=5:
    cinc+=1
    v-=5
while v>=2:
    dois+=1
    v-=2
while v>=1:
    um+=1
    v-=1
print(v)
print("{} nota(s) de R$ 100,00". format(cem))
print("{} nota(s) de R$ 50,00".format(cinq))
print("{} nota(s) de R$ 20,00".format(vint))
print("{} nota(s) de R$ 10,00".format(dez))
print("{} nota(s) de R$ 5,00".format(cinc))
print("{} nota(s) de R$ 2,00".format(dois))
print("{} nota(s) de R$ 1,00".format(um))