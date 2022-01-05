#WAP to calculate the compound interest.

p=int(input("Enter the principl amount"))
r=int(input("Enter the rate of interest"))
t=int(input("Enter the time required"))

amount = p * (pow((1 + r/100),t))
ci= amount - p
print("CI is",ci)
