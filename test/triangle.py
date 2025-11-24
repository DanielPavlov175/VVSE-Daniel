import math
a=int(input())
b=int(input())
c=int(input())
def area(a,b,c):
    S=int
    P=int
    h=int
    d=int
    if c==90:
        S=(a*b)/2
        P=a+b+math.sqrt(a*a+b*b-2*a*b*math.cos(c))
    else:
        h=b*math.sin(c)
        S=(a*h)/2
        d=math.sqrt(a*a+b*b-2*a*b*math.cos(c))
        P=a+b+d
    print(S)
    print(P)
print(area(a,b,c))