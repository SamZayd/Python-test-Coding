#Binary read-write with no exception(Single Record).
import pickle
def write():
    f=open("binaryf","wb")
    while True:
        roll=int(input("Enter roll number : "))
        name=(input("Enter name : "))
        per=float(input("Enter percentage"))