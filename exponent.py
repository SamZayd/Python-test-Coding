#Make user defined program to show exponent of x.

x=int(input("Enter the value of x\n"))
n=int(input("Enter the value for exponent\n"))
if(n < 0 and x == 0):
    print("\nThe value is not defined." )
else:
    print("\nThe value of ",x," to the power ",n," is ",x**n, ".")
