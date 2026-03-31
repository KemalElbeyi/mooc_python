class BankAccount:

    # The constructor
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

peters_account = BankAccount(100, "Peter Python")
print(peters_account.balance)

# Change the balance to 1500
peters_account.balance = 1500
print(peters_account.balance)

# Add 2000 to the balance
peters_account.balance += 2000
print(peters_account.balance)

# this function creates a new bank account object and returns it
def open_account(name: str):
    new_account =  BankAccount(0, name)
    return new_account

# this function adds the amount passed as an argument to the balance of the bank account also passed as an argument
def deposit_money_on_account(account: BankAccount, amount: int):
    account.balance += amount

peters_account = open_account("Peter Python")
print(peters_account.balance)

deposit_money_on_account(peters_account, 500)

print(peters_account.balance)

print("-----------------------------------")

class Pet:
    def __init__(self, name: str, species: str,year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth
# class tan bağımsız.
def new_pet(name: str, species: str, year_of_birth: int):
    object_pet = Pet(name, species, year_of_birth)
    return object_pet

fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)

print("---------------------------------")

class Book:
    def __init__(self, name: str, author: str,genre: str ,year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

def older_book(book1: Book, book2: Book):
    if book1.year > book2.year:
        print(f"High Adventure is older, it was published in {book2.year}")
    elif book1.year < book2.year:
        print(f"High Adventure is older, it was published in {book1.year}")
    else:
        print(f"{book1.name} and {book2.name} were published in {book2.year}")

older_book(python, everest)
older_book(python, norma)

def books_of_genre(books: list, genre: str):
    new_list = []
    for val in books:
        if val.genre == genre:
            new_list.append(val)
    return new_list
books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

print("Books in the crime genre:")
for book in books_of_genre(books, "crime"):
    print(f"{book.author}: {book.name}")