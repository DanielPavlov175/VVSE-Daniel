s=str(input())
halflen=int(len(s)/2)
i=0
j=1
check=1
if len(s)%2==0:
    for i in range (halflen):
        if s[i]!=s[len(s)-j]:
            print("Not a palindrome")
            check=0
            break
        else:
            j=j+1
else:
    for i in range (halflen+1):
        if s[i]!=s[len(s)-j]:
            print("Not a palindrome")
            check=0
            break
        else:
            j=j+1
if check==1:
    print("Is a palindrome")