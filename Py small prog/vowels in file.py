#WAP to count total number of vowels in the file.
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


def countv():
    f=open("abc.txt","r")
    r=f.read()
    s='A' ,'a' , 'E' , 'e' , 'I' , 'i' , 'O' ,'o' , 'U' , 'u'
    v=0
    for i in r:
        if i in s:
            v+=1
    print("number of vowels are ",v)
    f.close()

    
while True:
    ch=int(input("1.Write  2.Read  3.Count number of vowels  4.Exit \n please select any option:"))
    if(ch==1):
        write()
    elif(ch==2):
        read()
    elif(ch==3):
        countv()
    elif(ch==4):
        print("Exiting......")
        break
    else:
        print("Please select approprite option -_-")
        