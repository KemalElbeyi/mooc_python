import string
from random import randint

weekly_draw = []
while len(weekly_draw) < 7:
    new_rnd = randint(1, 40)
    if new_rnd not in weekly_draw:
        weekly_draw.append(new_rnd)

print(weekly_draw)

print("------------------------------------")
from random import shuffle

number_pool = list(range(1, 41))
shuffle(number_pool)
weekly_draw = number_pool[0:7]
print(weekly_draw)

print("------------------------------------")
from random import sample

number_pool = list(range(1, 41))
weekly_draw = sample(number_pool, 7)
print(weekly_draw)

print("------------------------------------")

def check(val,numarray:list):
    if val in numarray:
        return False
    else:
        return True
def lottery_numbers(amount:int,lower:int,upper:int):
    number_pool = []
    for i in range(amount):
        while True:
            val = randint(lower,upper)
            if check(val,number_pool):
                number_pool.append(val)
                break
    return sorted(number_pool)
for number in lottery_numbers(7, 1, 40):
    print(number)

print("------------------------------------")

def generate_password(lenght):
    password = ""
    for _ in range(lenght):
        char=chr(randint(97,122))#ASCI value of a is 97, z is 122
        password += char
    return password
for i in range(10):
    print(generate_password(8))

print("------------------------------------")
from random import choice

def improved_generate_password(lenght: int,amount1: bool,amount2: bool):
    password = []
    letters = string.ascii_lowercase
    numbers = string.digits
    specials = "!?=+-()#"
    password.append(choice(letters))
    if amount1:
        letters += numbers
        password += choice(numbers)
    if amount2:
        letters += specials
        password += choice(specials)
    while len(password) < lenght:
        password.append(choice(letters))
    shuffle(password)
    return "".join(password)
for i in range(10):
    print(improved_generate_password(3, True, True))

print("------------------------------------")

dice_sides = {
    "A" : [3, 3, 3, 3, 3, 6],
    "B" : [2, 2, 2, 5, 5, 5],
    "C" : [1, 4, 4, 4, 4, 4]}
def roll(die: str):
    return choice(dice_sides[die])

for i in range(20):
    print(roll("A"), " ", end="")
print()
for i in range(20):
    print(roll("B"), " ", end="")
print()
for i in range(20):
    print(roll("C"), " ", end="")
print()
def play(die1: str, die2: str, times: int):
    result1 = 0
    result2 = 0
    result3 = 0
    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            result1 += 1
        elif roll1 < roll2:
            result2 += 1
        else:
            result3 += 1
    return result1, result2, result3
result = play("A", "C", 1000)
print(result)
result = play("B", "B", 1000)
print(result)



