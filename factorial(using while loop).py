#WAP to find factorial of a number (using while loop).

num=int(input("Enter any number : "))
fact=1
a=1
while a<=num:
    fact=fact*a
    a+=1
print("Fctorial = ",fact)

