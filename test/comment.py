s=str(input())
i=0
count=0
for i in range(len(s)):
    if s[i]==' ':
        count+=1
if count>7:
    print("No")
else:
    s[0]=s[0]+32
    print(s)