n=int(input())
k=int(input())
numbers=[]
i=0
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    numbers.append(element)
i=0
for i in range(n):
    j=0
    for j in range(n):
        if i!=j:
            if (numbers[j]+numbers[i]>k):
                print(numbers[i]," ",numbers[j])
        