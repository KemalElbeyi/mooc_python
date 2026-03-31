#[<expression> for <item> in <series>]

numbers = [1,2,3,4,5]
strings = [str(number) for number in numbers]
print(strings)

print("--------------------------------")

from math import sqrt

def square_roots(numbers: list):
    new_list = [sqrt(num) for num in numbers]
    return new_list
lines = square_roots([1,2,3,4])
for line in lines:
    print(line)

print("--------------------------------")

def rows_of_stars(numbers: list):
    new_list = [num*"*" for num in numbers]
    return new_list

rows = rows_of_stars([4, 3, 2, 1, 10])
for row in rows:
    print(row)

print("--------------------------------")

class ExamResult:
    def __init__(self,name,grade1,grade2,grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
def best_results(results: list):
      return [max([result.grade1, result.grade2, result.grade3]) for result in results]

result1 = ExamResult("Peter", 5, 3, 4)
result2 = ExamResult("Pippa", 3, 4, 1)
result3 = ExamResult("Paul", 2, 1, 3)
results = [result1, result2, result3]
print(best_results(results))

print("--------------------------------")

def lengths(lists: list):
    new_list = [len(list) for list in lists]
    return new_list
lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
print(lengths(lists))

print("--------------------------------")

#[<expression> for <item> in <series> if <Boolean expression>]

numbers = [1, 1, 2, 3, 4, 6, 4, 5, 7, 10, 12, 3]
even_items = [item for item in numbers if item % 2 == 0]
print(even_items)

print("--------------------------------")

def remove_smaller_than(numbers: list, limit: int):
    return [num for num in numbers if num > limit]
numbers = [1, 65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))

print("--------------------------------")

def begin_with_vowel(words: list):
    return [item for item in words if item[0].lower() in ["a","e","i","o","u"]]
word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)

print("--------------------------------")
#[<expression 1> if <condition> else <expression 2> for <item> in <series>]
numbers = [1, -3, 45, -110, 2, 9, -11]
abs_vals = [number if number >= 0 else -number for number in numbers]
print(abs_vals)

print("--------------------------------")

class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.numbers = numbers
        self.week = week
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.numbers])
    def hits_in_place(self, numbers):
        return [number if number in self.numbers else -1 for number in numbers]

week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
my_numbers = [1,4,7,11,13,19,24]
print(week5.number_of_hits(my_numbers))

week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]
print(week8.hits_in_place(my_numbers))

print("--------------------------------")

def filter_forbidden(string: str, forbidden: str):
    return "".join([character for character in string if character not in forbidden])
sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)

print("--------------------------------")

class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int,description: str):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
        self.description = description
def cheaper_properties(properties: list,reference: RealProperty):
    return [(prop,reference.square_metres*reference.price_per_sqm-prop.square_metres*prop.price_per_sqm)for prop in properties if prop.square_metres*prop.price_per_sqm < reference.square_metres*reference.price_per_sqm]
a1 = RealProperty(1, 16, 5500, "Central studio")
a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
a5 = RealProperty(4, 105, 1700, "Loft in a small town")
a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

properties = [a1, a2, a3, a4, a5, a6]

print(f"cheaper options when compared to {a3.description}:")
for item in cheaper_properties(properties, a3):
    print(f"{item[0].description:35} price difference {item[1]} euros")
print("--------------------------------")
#Comprehensions and dictionaries
#{<key expression> : <value expression> for <item> in <series>}

def lengths(strings: list):
    return {string : len(string) for string in strings}
word_list = ["once", "upon" , "a", "time", "in"]
word_lengths = lengths(word_list)
print(word_lengths)

print("--------------------------------")


