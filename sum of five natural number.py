#TO print the sum of five natural number.

s=0
a=int(input("Enter the starting ntural number :- "))
b=int(input("Enter the ending ntural number :- "))
for i in range(a,b):
    s=s+i
    print(i)
print("Sum of a = ",a," TO b = ",b," is ",s,".")    
    