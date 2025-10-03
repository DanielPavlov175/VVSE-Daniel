n=int(input())
daytime=str(input())
if n<20:
    print("Taxi only")
    if daytime=='day':
        price=(0.79*n)+0.7
    elif daytime=='night':
        price=(0.9*n)+0.7
elif n>=20 and n<100:
    print("Bus is the best option")
    price=0.09*n
elif n<=100:
    print("Train is the best option")
    price=0.06*n
print(price)