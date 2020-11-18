vezes=int(input())
a=b=0
for i in range(0,vezes):
    num=int(input())
    if num>=10 and num<=20:
        a+=1
    else:
        b+=1
print("{} in".format(a))
print("{} out".format(b))