
while True:
    number1 = int(input("Please type in a number, -1 to quit "))
    if number1 == -1:
        break

password = 1234
a = 0
while True:
    a += 1
    password1 = int(input("Please type in a password: "))
    if password1 == password and a > 1:
        print(f"Correct, it took you {a} attemps")
        break
    elif password1 == password and a == 1:
        print("Correct, it took you one single attempt")
        break
    elif a > 2 :
        print("Block!")
        break
    else:
        print("Wrong")

print("-------------------------------------")

upperLimit=int(input("Sayı girin:"))
base = int(input("Base:"))
temp = base
while True:
    print(base)
    base *= temp
    if upperLimit <= base:
        break

print("-------------------------------------")

n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

print("-------------------------------------")

word1 = input("Please type in a word: ")
word2 = input("Please type in a word: ")
if len(word1) < len(word2):
    print(f"{word1} is shorter than {word2}")
elif len(word1) > len(word2):
    print(f"{word2} is longer than {word1}")
else :
    print(f"Both {word1} and {word2} have equal length")
print("First character: "+word1[0])
print("Last character: "+word1[-1])

print("-------------------------------------------")

word = input("Please type in a word: ")
index = len(word)-1
while index >= 0:
    print(word[index])
    index -= 1
index = -1
while index >= -len(word):
    print(word[index])
    index -= 1

print("-------------------------------------------")

width = int(input("Width:"))
height = int(input("Height:"))
while height > 0:
    print("#" * width)
    height -= 1

print("-------------------------------------------")

word3 = input("Please type in a word: ")
print(len(word3))
if len(word3) % 2 != 0:
    print("*" * 30)
    index1=int((28-len(word3))/2)
    index2=index1 + 1
    print("*" + " " * index1 + word3 + " " * index2 + "*")
    print("*" * 30)
else:
    print("*" * 30)
    print("*" + word3 + "*")
    print("*" * 30)

print(word3[:3])
print(word3[3:])

if "i" in word3:
    print("Found it")
else:
    print("Not found")

index3=1
while index3<=len(word3):
    print(word3[:index3])
    index3+=1

print("-------------------------------------------")

word4 = input("Please type in a word: ")
while True:
    ch = input("Please type in a character: ")
    index3 = word4.find(ch)
    if index3 == -1:
        print("Not found")
        break
    else:
        print(word4[index3:index3 + 3])
        print(index3)

print("-------------------------------------------")

sentence = input("Please type in a sentence: ")
sentence = " "+sentence
i = 0
while i < len(sentence)-1:
    if sentence[i] == " ":
        print(sentence[i+1])
    i += 1


print("-------------------------------------------")

number3 = int(input("Please type in a number: "))
i = 1
while i <= number3:
    if i == number3 and i%2 == 1:
        print(i)
    elif i%2 == 1:
        print(i+1)
        print(i)
    i+=1

# Print the numbers in flipped order
for i in range(1, number3 + 1, 2):
    if i + 1 <= number3:
        print(i + 1)  # Print the second number of the pair first
    print(i)  # Then print the first number of the pair

print("-------------------------------------------")

number4 = int(input("Please type in a number: "))
i=1

while i<=number4:
    if i==number4:
        print(i)
    else:
        print(i)
        print(number4)
    number4 -= 1
    i+=1






