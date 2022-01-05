#To know whether the year is leap year or not.

a=int(input("Enter the year : "))
if(a%4==0):
    if(a%100==0):
        if(a%400==0):
            print("The year is leap year .")
        else:
            print("The year is not a leap year .")
    else: 
        print("The year is leap year. ")
else:
    print("The year is not a leap year .")