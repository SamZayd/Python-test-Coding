#WAP to count the number of uppercase and lowercase letters separately.
def countu():
    f=open("test.txt","r")
    r=f.read()
    count=0
    for i in r:
        if(i.isupper):
            count+=1
    print("Text is ",r)        
    print("count is ",count)        

countu()

