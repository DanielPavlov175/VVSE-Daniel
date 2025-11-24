n=0
while n<1 or n>1000:
    n=int(input())
pay=int
p1=0
p2=0
p3=0
p4=0
p5=0
i=0
for i in range (n):
    pay=int(input())
    if pay<200:
        p1+=1
    if pay>=200 and pay<400:
        p2+=1
    if pay>=400 and pay<600:
        p3+=1
    if pay>=600 and pay<800:
        p4+=1
    if pay>=800:
        p5+=1
percent1=(p1/n)*100
percent2=(p2/n)*100
percent3=(p3/n)*100
percent4=(p4/n)*100
percent5=(p5/n)*100
print(percent1)
print("%")
print(percent2)
print("%")
print(percent3)
print("%")
print(percent4)
print("%")
print(percent5)
print("%")