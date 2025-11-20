lenght=int(0)
count=int(0)
avr=float
n=int(input())
for i in range (n):
    s=str(input())
    lenght=lenght+len(s)
    count=count+1
avr=lenght/count
print(avr)