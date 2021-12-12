#Range Function
a=1
b=11
c=100*2
sum=0

for i in range(a,b):
    sum=sum+i*i
    print (i*i,end='+')

print ("\n=",sum)