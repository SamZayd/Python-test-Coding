f=open("test.txt","r")
s1=f.read()
size=0
tsize=0
print(s1)
while s1:
    tsize=tsize+len(s1)
    size=size+len(s1.strip())
    print(size)
    print(tsize)
    f.close()

