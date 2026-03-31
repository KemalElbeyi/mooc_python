def times_ten(start_index: int, end_index: int):
    list = {}
    for i in range(start_index, end_index+1):
        list[i] = i*10
    return list
list = times_ten(3,6)
print(list)

print("---------------------------------------")

def factorial(number: int):
    list[number] = 1
    for i in range(1,number+1):
        list[number] *= i
    return list
list = factorial(5)
print(list[5])

print("---------------------------------------")

def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
        initial = word[0]
        # initialize a new list when the letter is first encountered
        if initial not in groups:
            groups[initial] = []
        # add the word to the appropriate list
        groups[initial].append(word)
    return groups
word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]
groups = categorize_by_initial(word_list)

for key, value in groups.items():
    print(f"words beginning with {key}:")
    for word in value:
        print(word)

print("---------------------------------------")

def histogram(word:str):
    list = {}
    for letter in word:
        if letter not in list:
            list[letter] = ""
        list[letter] += "*"
    for key,value in list.items():
        print(f"{key}: {value}")
histogram("statistically")

print("---------------------------------------")

def phoneBook():
    list = {}
    while True:
        num = int(input("command(1 search, 2 add, 3 quit):"))
        if num == 1:
            name = input("name: ").lower()
            if name in list:
                print(list[name])
            else:
                print("no number")
        elif num == 2:
            name = input("name: ").lower()
            number = int(input("number: "))
            list[name] = number
            print("ok!")
        else:
            print("quiting...")
            break
phoneBook()
def phoneBook2():
    list = {}
    while True:
        num = int(input("command(1 search, 2 add, 3 quit):"))
        if num == 1:
            name = input("name: ").lower()
            if name in list:
                for key, value in list.items():
                    for i in value:
                        print(i)
            else:
                print("no number")
        elif num == 2:
            name = input("name: ").lower()
            number = int(input("number: "))
            if name in list:
                list[name].append(number)
            else:
                list[name] = [number]
            print("ok!")
        else:
            print("quiting...")
            break
phoneBook2()

print("---------------------------------------")

def invert(dictionary: dict):
    keys = list(dictionary.keys())  # Anahtarları listeye alıyoruz, çünkü sözlük üzerinde iterasyon yaparken boyut değişebilir.
    for key in keys:
        value = dictionary[key]
        dictionary[value] = key
        del dictionary[key]

s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)

print("---------------------------------------")

def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    numbers = {}
    for i in range(0,10):
        numbers[i] = ones[i]
    for i in range(10,20):
        numbers[i] = teens[i-10]
    for i in range(20,100):
        if i%10 != 0:
            numbers[i] = tens[i//10]+"-"+ones[i%10]
        else:
            numbers[i] = tens[i//10]
    return numbers
numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[20])
print(numbers[45])
print(numbers[99])
print(numbers[0])

print("---------------------------------------")

def add_movie(database: list,name: str,director: str,year: int,runtime: int):
    movie = {"name":name,"director":director,"year":year,"runtime":runtime}
    database.append(movie)
database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(database)

print("---------------------------------------")

def find_movies(database: list, search_term: str):
    movies = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            movies.append(movie)
    return movies
database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

my_movies = find_movies(database, "python")
print(my_movies)







