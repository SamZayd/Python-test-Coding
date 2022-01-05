#WAP to read a text file line by line and display each word separated by a #.
def write():
    f=open("abc.txt","w")
    while True:
        s=input("Enter a line : ")
        f.write(s+"\n")
        ch=input("More lines? \n Please enter yes or no. ")
        if (ch=="no" or ch=="No" or ch=="NO" or ch=="N"):
            break
        elif(ch=="yes" or ch=="Yes" or ch=="YES" or ch=="Y"):
            continue
        f.close()
    
   
def read():
    f=open("abc.txt","r")
    r=f.read()
    print(r)
    f.close()
    
def display():
    f=open("abc.txt","r")
    str=f.read()
    a=str.replace(' ','#')
    print(a)
    f.close()
    
while True:
    ch=int(input("1.Write  2.Read  3.to display each word separated by a #  4.Exit \n please select any option:"))
    if(ch==1):
        write()
    elif(ch==2):
        read()
    elif(ch==3):
        display()
    elif(ch==4):
        print("Exiting......")
        break
    else:
        print("Please select approprite option -_-")
    