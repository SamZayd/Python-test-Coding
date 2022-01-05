#WAP to count number of words in a file.
f=open("test.txt","r")
r=f.read()
s=r.split()
length=len(s)
print(r)
print("\nWord count is ",length)
f.close()
