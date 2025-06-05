numius = 90
guss = 0
while guss != numius:
    guss = int(input("enter number plz:"))
    if guss < numius:
        print("its to small")
    elif guss > numius:
        print("its to big")
    if numius - guss == 1:
        print("your close!")
    if guss - numius == 1:
        print("your close!!")
    elif guss == numius:
        print("you won")