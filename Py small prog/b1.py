#Single record.
import pickle
def write():
    f=open("binaryfile","wb")
    while True:
        roll=int(input("Enter roll number : "))
        name=input("Enter name : ")
        per=float(input("Enter percentage : "))
        record=[roll,name,per]
        pickle.dump(record,f)
        ch=input("More record?? \n Please enter yes or no \n")
        if(ch=="no" or ch=="NO" or ch=="No"):
            break
    f.close()
def read():
    f=open("binaryfile","rb")
    try:
        while True:
            record=pickle.load(f)
            print(record)
    except EOFError:
        print("EOF reached")
    f.close()
write()
read()
        
    