from math import sqrt,pow

def hypotenuse(leg1: float, leg2: float):
    return sqrt(pow(leg1, 2) + pow(leg2, 2))
print(hypotenuse(3,4))
print(hypotenuse(5,12))
print(hypotenuse(1,1))

print("---------------------------------------")
from string import ascii_letters,punctuation

def separate_characters(my_string: str):
    letters = ""
    puncts = ""
    others = ""
    for char in my_string:
        if char in ascii_letters:
            letters += char
        elif char in punctuation:
            puncts += char
        else:
            others += char
    return letters, puncts, others

parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])

print("---------------------------------------")
from fractions import Fraction

def fractionate(amount :int):
    new_list = []
    for i in range(amount):
        new_list.append(Fraction(1,amount))
    return new_list
for p in fractionate(3):
    print(p)

print()

print(fractionate(5))