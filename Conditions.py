kosul = True
while(kosul):
    try:
        number = int(input("Enter a number: "))
        if number > 100:
            print("the number is greater than one hundred.")
            number = number - 100
            print("that is value decreased by one hundred.")
            print("its value is now "+ str(number))
        print(str(number)+" must be my lucky number")
        kosul = False
    except ValueError:
        print("Please enter a number.")

name1 = input("What is your name? ")
age1 = int(input("Enter your age: "))
name2 = input("What is your name? ")
age2 = int(input("Enter your age: "))
if age1 > age2:
    print(f"{name1}s age is greater than {name2} age.")
elif age2 > age1:
    print(f"{name2}s age is greater than {name1} age.")
else:
    print("Your age is equal to your age.")

print("------------------------------------------")

letter1 = input("Enter a letter: ")
letter1 = letter1.upper()
letter2 = input("Enter a letter: ")
letter2 = letter2.upper()
letter3 = input("Enter a letter: ")
letter3 = letter3.upper()
if (letter1 > letter2 and letter1 < letter3) or (letter1 > letter3 and letter1 < letter2):
    print("The letter in the middle is "+ letter1)
elif (letter2 > letter1 and letter2 < letter3) or (letter2 > letter3 and letter2 < letter1):
    print("The letter in the middle is "+ letter2)
else:
    print("The letter in the middle is "+ letter3)
