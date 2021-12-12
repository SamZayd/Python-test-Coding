#WAP to count the number of lines in the file.
def countl():
    f=open("test.txt","r")
    l=f.readlines()
    print(l)
    print("number of lines=",len(l))
    f.close()
countl()