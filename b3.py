#WAP to display those records where percentage is between 80 and 90(both included).
import pickle
def write():
    f=open("binf","wb")
    record=[]
    while True:
        roll=int(input("Enter roll number : "))
        name=input("Enter name : ").upper()
        sec=input("Enter section :  ").upper()
        per=float(input("Enter percentage : "))
        r=[roll,name,sec,per]
        record.append(r)
        ch=input("More records?? \n please enter yes or no \n")
        if ch=="no" or ch=="NO" or ch=="No":
            break;     
    pickle.dump(record,f)
    f.close()

def read():
    f=open("binf","rb")
    record=pickle.load(f)
    print("Displaying record... \n",record)
    f.close()

def search():
    f=open("binf","rb")
    record=pickle.load(f)
    for i in record:
        if i[3]>=80 and i[3]<=90:
            print(i)
    f.close()    
write()
read()
search()    

    