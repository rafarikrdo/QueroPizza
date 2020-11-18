#def achaNumeros(lista):
 #   for i in range(0, len(lista)):
  #  return i

vezes=int(input())
a=0
list=[]
for i in range(0,vezes):
    num=int(input())
    list.append(num)
    list.sort()
for i in range(0, vezes):
    a = list.count(list[i])
    if list[i] != list[i-1]:
        print("{} aparece {} vez(es)".format(list[i], a))
    else:
        not print()