print("1. + ")
print("2. - ")
print("3. * ")
print("4. / ")
print("5. //")
print("6. % ")

number1 = int(input("Enter number n.1:"))
oparation = int(input("Enter oparation:"))
number2 = int(input("Enter number n.2:"))

if oparation == 1:
    print(number1 + number2)
elif oparation == 2:
    print(number1 - number2)
elif oparation == 3:
    print(number1 * number2)
elif oparation == 4:
    print(number1 / number2)
elif oparation == 5:
    print(number1 // number2)
elif oparation == 6:
    print(number1 % number2)
