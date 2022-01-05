import pickle
def write():
    f=open("pro","wb")
    record=[]
    while True:
        name=input("Enter product name : ")
        price=float(input("Enter price : "))
        r={"NAME":name,"PRICE":price}
        record.append(r)
        ch=input("More records?? \n Please enter yes or no \n")
        if(ch=="no" or ch=="NO" or ch=="No"):
            break;
    pickle.dump(record,f)
    f.close()
def read():
    f1=open("newpro","wb")
    record=pickle.load(f1)
    print(record)
    f1.close()
def transfer():
    f=open("pro","rb")
    f1=open("newpro","rb")
    record=pickle.load(f)
    t=[]
    for i in record:
        if i["PRICE"]<100:
            t.append(i)
    pickle.dump(t,f1)
write()
read()
transfer()
read()
    