class Compute:
    def Factorial(a):
        f=1
        for i in range(a):
            f=f*(a-i)
        return f
    def Sum(n):
        s=0
        a=1
        for i in range(n):
            s=s+a
            a=a+1
        return s
    def tableMult(a):
        for i in range(11):
            print(a,"*",i,"=",a*i)
    def listDiv(a):
        l=list()
        for i in range(a):
            if i>1:
                if a%i==0:
                   l.append(i)
        return l
print(Compute.listDiv(120))