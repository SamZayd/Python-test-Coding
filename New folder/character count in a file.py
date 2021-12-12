f=open("test.txt","r")
r=f.read()
print(r)
l=r.split()
length=len(l)
count=0
for i in l: 
    count+=len(i)
print("Word count is",length,".")
print("Character count is {} .".format(count))
    
f.close
    