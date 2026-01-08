def read():
    f=open("text.txt","r")
    d=f.readlines()
    f.close
    return d
def write():
    l=["hello","world","how","are","you"]
    for i in range(len(l)-1):
        if i%2==0:
            l.pop(i)
    print(l)
print(read())
print(write())