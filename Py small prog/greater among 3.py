#To find weather three numbers are greater or equal.

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
if(a>b and a>c):
    print(a,"is greater than both",b,"and",c)
elif(b>a and b>c):
    print(b,"is greater than both",a,"and",c)
elif(c>a and c>b):
    print(c,"is greater than both",a,"and",b)
else:
    print("All are equal.")
