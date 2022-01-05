#WAP to find the distance between two coordinate
from cmath import sqrt
x1=int(input("enter the value of x1 : "))
x2=int(input("enter the value of x2 : "))
y1=int(input("enter the value of y1 : "))
y2=int(input("enter the value of y2 : "))
d=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print("distance between the given coordiate is ",d)
