#Wap to check vowel or consonant.

y=str(input("Enter the alphabet :- "))
x=y[0]

if(x=='A' or x=='a' or x=='E' or x=='e' or x=='I' or x=='i' or x=='O' or x=='o' or x=='U' or x=='u' ):
    print(x,"is a vowel.")    
else:
    print(x,"is a consonant.")