# append(sayı),insert(i,sayı),pop(index),remove(sayı)

word_list = []
while True:
    word = input("Word: ")
    if word in word_list:
        break
    word_list.append(word)
print(word_list)
print(len(word_list))

print("----------------------------------------")

my_list = [2,5,1,2,4]
my_list.sort()
print(my_list)
my2_list = [2,5,1,2,4]
print(sorted(my2_list))

print("----------------------------------------")

def add_remove():
    list = []
    i=1
    while True:
        text=input("Enter a word: ")
        if text == "add":
            list.append(i)
            print(list)
            i+=1
        elif text == "remove":
            list.pop()
            print(list)
            i-=1
        elif text == "exit":
            print("Goodbye")
            break
add_remove()

print("----------------------------------------")

def list_of_stars(inputList):
    for variable in inputList:
        print("*" * variable)

list_of_stars([3, 2, 5])
print("----------------------------------------")

def anagrams(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
print(anagrams("tame", "team"))

print("----------------------------------------")

def palindromes(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindromes("kemel"))

print("----------------------------------------")

def sum_of_positives(m_list:list):
    result = 0
    for number in m_list:
        if number > 0:
            result+=number
    return result
m_list = [1, -2, 3, -4, 5]
print(sum_of_positives(m_list))

print("----------------------------------------")

def even_numbers(my_list):
    even_list = []
    for var in my_list:
        if var % 2 == 0:
            even_list.append(var)
    return even_list
my_list = [1,2,3,4,5,6,7,8,9]
new_list = even_numbers(my_list)
print(my_list)
print(new_list)

print("----------------------------------------")

def distinct_numbers(my_list):
    new_list = []
    for var in my_list:
        if var not in new_list:
            new_list.append(var)
    new_list.sort()
    return new_list
my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list))

print("----------------------------------------")

def length_of_longest(my_list):
    longest = len(str(my_list[0]))
    for i in range(1, len(my_list)):
        if len(str(my_list[i])) > longest:
            longest = len(str(my_list[i]))
    return longest

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = length_of_longest(my_list)
print(result)

print("----------------------------------------")

def formatted(my_list):
    new_list = []
    for var in my_list:
        new_list.append(f"{var:.2f}")
    return new_list
my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)

print("----------------------------------------")

def everything_reversed(my_list):
    new_list = []
    new_list.reverse()
    iter = len(my_list)-1
    while iter >= 0:
        new_list.append(my_list[iter][::-1])
        iter -= 1
    return new_list
my_list = ["Ustam", "şifa", "yapmış", "hocam"]
new_list = everything_reversed(my_list)
print(new_list)
print(my_list[1][::-1])


print("----------------------------------------")

my_string = "Python is fun"

# Replaces the substring and stores the result in the same variable
my_string = my_string.replace("Python", "Java")
print(my_string)

print("----------------------------------------")

def most_common_character(text1):
    max_count = 0
    ch=""
    for var in text1:
        count = text1.count(var)
        if count > max_count:
            max_count = count
            ch = var
    return ch
print(most_common_character("abcdbdeea"))

print("----------------------------------------")

def no_vowels(text):
    new_text=""
    for var in text:
        if var not in ["a", "e", "i", "o", "u"]:
            new_text += var
    return new_text
print(no_vowels("this is an example"))

print("----------------------------------------")

def no_shouting(list):
    new_list = []
    for var in list:
        if not var.isupper():
            new_list.append(var)
    return new_list
my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
print(no_shouting(my_list))

print("----------------------------------------")

def longest_series_of_neighbours(list):
    count = 1
    max_count = 1
    for i in range(len(list)-1):
        if abs(list[i] - list[i + 1]) == 1:
            count+=1
            max_count = max(count, max_count)
        else:
            count=1
    return max_count
my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))












