a, b, c= map(int, input().split())
delta0=b-a
delta1=c-b
if a>b:
    if b <= c: #ok
        print(":)")
    if b > c:
        if delta1 > delta0:
            print(":)")
        if delta1 <= delta0:
            print(":(")
if a<b:
    if b>=c: #ok
        print(":(")
    if b < c:
        if delta1 < delta0:
            print(":(")
        if delta1 >= delta0:
            print(":)")
if a == b:
    if b<c:
        print(":)")
    if b>c:
        print(":(")
    if b == c:
        print(":(")