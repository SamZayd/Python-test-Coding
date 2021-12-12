#WAP to count number of words in a file. 
def countw():
    f=open("test.txt","r")
    r=f.read()
    s=r.split()
    print(r)
    print("Number of words = ",len(s))
    f.close
countw()
