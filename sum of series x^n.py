
y=int(input("Enter the range value :"))
x=y+1
sum=0
for i in range(1,x):
    print((i**i),end="+")
    sum=sum+(i**i)
print("\nSum = ",sum)
