a=int(9)
b=int(1)
pages=int(0)
n=int(input())
while 1:
    if n-a*b<0:
        print(n/b+pages)
        break
    else:
        n=n-a*b
        pages=pages+a
        a=a*10
        b=b+1