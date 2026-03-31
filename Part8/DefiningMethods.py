from Part5.References import add_number


class BankAccount:

    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

    # This method adds the annual interest to the balance of the account
    def add_interest(self):
        self.balance += self.balance * self.annual_interest

# The class BankAccount is defined in the previous example
peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
paulas_account = BankAccount("99999-999", "Paula Pythonen", 1500.0, 0.05)
pippas_account = BankAccount("1111-222", "Pippa Programmer", 1500.0, 0.001)

# Add interest on Peter's and Paula's accounts, but not on Pippa's
peters_account.add_interest()
paulas_account.add_interest()

# Print all account balances
print(peters_account.balance)
print(paulas_account.balance)
print(pippas_account.balance)

print("-------------------------------")

class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value -= 1
        if self.value < 0:
            print("Sıfıra ulaşıldı")
            self.value = 0

    def set_to_zero(self):
        self.value = 0

    def increase(self,num = 1):
        self.value += num

    def reset_original_value(self):
        self.value = self.initial_value

counter = DecreasingCounter(10)
counter.print_value()
counter.decrease()
counter.print_value()
counter.increase(2)
counter.print_value()
counter.reset_original_value()
counter.print_value()
counter.set_to_zero()
counter.print_value()

print("-------------------------------")

class Person:
    def __init__(self, name: str):
        self.name = name
    def return_first_name(self):
        return self.name.split()[0]
    def return_last_name(self):
        return self.name.split()[1]
if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())

print("-------------------------------")

class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.sum_num = 0
        self.average_num = 0
        self.even_num = 0
        self.odd_num = 0
    def add_number(self, number: int):
        if number % 2 == 0:
            self.even_num += number
        else:
            self.odd_num += number
        self.numbers += number
        self.count += 1
        self.sum_num += number
    def count_numbers(self):
        return self.count
    def get_sum(self):
        if self.count == 0:
            return 0
        return self.sum_num
    def average(self):
        if self.count == 0:
            return 0
        return self.sum_num / self.count
stats = NumberStats()
while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    stats.add_number(num)
print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats.even_num)
print("Sum of odd numbers:", stats.odd_num)


