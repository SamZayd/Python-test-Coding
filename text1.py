#WAP to count total number of alphabets,numbers,and special characters.
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
    
def count():
    f=open("abc.txt","r")
    r=f.read()
    a=d=s=0
    for i in range(len(r)):
        if(r[i].isalpha()):
            a+=1
        elif(r[i].isdigit()):
            d+=1
        else:
            s+=1
    print("Number of alphbets= ",a,"\n Number of digits= ",d,"\n number of special character= ",s)
    f.close()
    
while True:
    ch=int(input("1.Write  2.Read  3. to Count number alphabets,digits and special character  4.Exit \n please select any option:"))
    if(ch==1):
        write()
    elif(ch==2):
        read()
    elif(ch==3):
        count()
    elif(ch==4):
        print("Exiting......")
        break
    else:
        print("Please select approprite option.")