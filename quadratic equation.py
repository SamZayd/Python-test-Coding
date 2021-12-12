from cmath import sqrt
a=int(input(" Enter the value of a : ")) 
b=int(input(" Enter the value of b : "))
c=int(input(" Enter the value of c : "))  
d=b*b-4*a*c
print("The value of discriminant is ",d)
p=(-b+sqrt(d))/2*a
q=(-b-sqrt(d))/2*a
if(d>0):
    print("The roots are ",p,q,"and the roots are real and distinct.")
elif(d==0):
    print("The roots are",p,q,"and the roots are equal and real.")
else:
    print("The roots are complex and imaginary. ")
        
        