#To find leap year between two years.

a=int(input("Enter the starting search year : "))
b=int(input("Enter the last search year :  "))
c = 0
for i in range(a,b):
    if( i%4==0):
        print(i,end=",")
        c = 1
if(c == 0):
    print("There is no leap year between",a,"and",b,".")