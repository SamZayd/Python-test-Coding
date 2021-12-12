#Global variable exammple.
def fun():
    global s #accessing/making global variable for fun().
    print(s)
    s="I love India!"#chaning global variable value.
    print(s)
s="I love World!"
fun()
print(s)