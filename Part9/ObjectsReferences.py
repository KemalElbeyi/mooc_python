class Car:
    def __init__(self,make: str,top_speed: int):
        self.make = make
        self.top_speed = top_speed
def fastest_car(cars: list):
    fast = cars[0]
    for car in cars:
        if car.top_speed > fast.top_speed:
            fast = car
    return fast.make

car1 = Car("Saab", 195)
car2 = Car("Lada", 110)
car3 = Car("Ferrari", 280)
car4 = Car("Trabant", 85)
cars = [car1, car2, car3, car4]
print(fastest_car(cars))

print("-------------------------------")

class ExamSubmission:
    def __init__(self,examinee: str,points: int):
        self.examinee = examinee
        self.points = points
    def __str__(self):
        return f"ExamSubmission (examinee: {self.examinee}, points: {self.points})"
def passed(submission: list,lowest_passing: int):
    pas = []
    for sub in submission:
        if sub.points >= lowest_passing:
            pas.append(sub)
    return pas
s1 = ExamSubmission("Peter", 12)
s2 = ExamSubmission("Pippa", 19)
s3 = ExamSubmission("Paul", 15)
s4 = ExamSubmission("Phoebe", 9)
s5 = ExamSubmission("Persephone", 17)
passes = passed([s1, s2, s3, s4, s5], 15)
for passing in passes:
    print(passing)

print("-------------------------------")

class Person:
    def __init__(self,name: str,age: int,height: int,weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
class BabyCentre:
    def __init__(self):
        self.weigh_count = 0
    def weigh(self,person: Person):
        self.weigh_count += 1
        return person.weight
    def feed(self,person: Person):
        person.weight += 1
    def weigh_ins(self):
        return self.weigh_count

baby_centre = BabyCentre()
eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)
print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")
print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
baby_centre.feed(eric)
baby_centre.feed(eric)
baby_centre.feed(eric)
print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
baby_centre.weigh(eric)
baby_centre.weigh(eric)
print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

print("-------------------------------")

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    def deposit_money(self, amount: float):
        self.balance += amount
    def subtract_from_balance(self, amount: float):
        if self.balance > amount:
            self.balance -= amount
            return True
        else:
            return False

card = LunchCard(10)
print("Balance", card.balance)
result = card.subtract_from_balance(8)
print("Payment successful:", result)
print("Balance", card.balance)
result = card.subtract_from_balance(4)
print("Payment successful:", result)
print("Balance", card.balance)

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0
    def eat_lunch(self,payment: float):
        if payment >= 2.5:
            payment -= 2.5
            self.funds += 2.5
            self.lunches += 1
        return payment
    def eat_special(self,payment: float):
        if payment >= 4.3:
            payment -= 4.3
            self.funds += 4.3
            self.specials += 1
        return payment
    def eat_lunch_lunchcard(self,card: LunchCard):
        if card.balance > 2.5:
            card.balance -= 2.5
            self.lunches += 1
            return True
        else:
            return False
    def eat_special_lunchcard(self,card: LunchCard):
        if card.balance > 4.3:
            card.balance -= 4.3
            self.specials += 1
            return True
        else:
            return False
    def deposit_money_on_card(self,card: LunchCard,amount: float):
        card.balance += amount
        self.funds += amount

exactum = PaymentTerminal()

card = LunchCard(2)
print(f"Card balance is {card.balance} euros")

result = exactum.eat_special_lunchcard(card)
print("Payment successful:", result)

exactum.deposit_money_on_card(card, 100)
print(f"Card balance is {card.balance} euros")

result = exactum.eat_special_lunchcard(card)
print("Payment successful:", result)
print(f"Card balance is {card.balance} euros")

print("Funds available at the terminal:", exactum.funds)
print("Regular lunches sold:", exactum.lunches)
print("Special lunches sold:", exactum.specials)

print("-------------------------------")

class RealProperty:
    def __init__(self, rooms: int,square_metres: int,price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    def bigger(self,compared_to):
        if self.square_metres > compared_to.square_metres:
            return True
        else:
            return False

    def price_difference(self, compared_to):
        return abs(self.square_metres*self.price_per_sqm-compared_to.square_metres*compared_to.price_per_sqm)
    def more_expensive(self,compared_to):
        if self.square_metres*self.price_per_sqm > compared_to.square_metres*compared_to.price_per_sqm:
            return True
        else:
            return False

central_studio = RealProperty(1, 16, 5500)
downtown_two_bedroom = RealProperty(2, 38, 4200)
suburbs_three_bedroom = RealProperty(3, 78, 2500)

print(central_studio.bigger(downtown_two_bedroom))
print(suburbs_three_bedroom.bigger(downtown_two_bedroom))
print(central_studio.price_difference(downtown_two_bedroom))
print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))
print(central_studio.more_expensive(downtown_two_bedroom))
print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))






