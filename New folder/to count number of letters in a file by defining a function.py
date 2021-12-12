#WAP to count number of letters in a file.
def counta():
    f=open("test.txt","r")
    r=f.read()
    s=r.split()
    count=0
    Others=0
    print(s)
    for i in s:
        for j in i:
            if(i[j].isalpha()):
                count+=1
                print("Number of letters= ",count)
            else:
                Others+=1
                print("Number of other characters= ",Others)
    f.close()
counta()