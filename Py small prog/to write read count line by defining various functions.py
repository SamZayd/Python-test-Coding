#WAP to write in a file.
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
        
        
#WAP to read file.   
def read():
    f=open("abc.txt","r")
    r=f.read()
    print(r)
    f.close()
    
    
#WAP  to check number of lines in a file.    
def countl():
    f=open("abc.txt","r")
    p=f.readlines()
    print("Number of lines=",len(p))
    f.close
    
    
#WAP to count number of words in a file. 
def countw():
    f=open("abc.txt","r")
    r=f.read()
    s=r.split()
    print("Number of words = ",len(s))
    f.close

#WAP to count number of character in a file.
def countC():
    f=open("abc.txt","r")
    r=f.read()
    s=r.split()
    count=0
    for i in s:
        count+=len(i)
    print("Number of characters = ",count)
    f.close()
    
def countWInLine():
    f=open("abc.txt","r")
    r=f.readline()
    c=0
    s=r.split()
    for i in s:
        c+=1
    print("number of words in line is ",c)
    
while True:
    ch=int(input("1.Write  2.Read  3.Count number of lines  4.count number of words 5.count number of character 6.to count number of words in line 7.Exit \n Please select any option:"))
    if(ch==1):
        write()
    elif(ch==2):
        read()
    elif(ch==3):
        countl()
    elif(ch==4):
        countw()
    elif(ch==5):
        countC()
    elif(ch==6):
        countWInLine()
    elif(ch==7):
        print("Exiting......")
        break
    else:
        print("Please select approprite option -_-")
        
        
        
    
    
    
                 
        