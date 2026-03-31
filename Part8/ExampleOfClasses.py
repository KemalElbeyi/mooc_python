'''class Stopwatch:
    def __init__(self):
        self.minutes = 0
        self.seconds = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0

    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"
watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()

print("--------------------------------")

class Clock:
    def __init__(self,hours: int,minutes: int,seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                if self.hours == 24:
                    self.hours = 0

    def set(self,hours: int,minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)

print("--------------------------------")

class LunchCard:
    def __init__(self,balance: float):
        self.balance = balance
    def eat_lunch(self):
        if self.balance >= 2.6:
            self.balance -= 2.6
            return True
        return False
    def eat_special(self):
        if self.balance >= 4.6:
            self.balance -= 4.6
            return True
        return False
    def deposit_money(self,amount: float):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        else:
            self.balance += amount
    def __str__(self):
        return f"Balance {self.balance:.1f} tl"
parker_card = LunchCard(20)
mustafa_card = LunchCard(30)
parker_card.eat_special()
mustafa_card.eat_lunch()
print(f"Parker: {parker_card}\nMustafa: {mustafa_card}")
parker_card.deposit_money(20)
mustafa_card.eat_special()
print(f"Parker: {parker_card}\nMustafa: {mustafa_card}")
parker_card.eat_lunch()
parker_card.eat_lunch()
mustafa_card.deposit_money(50)
print(f"Parker: {parker_card}\nMustafa: {mustafa_card}")

print("--------------------------------")
'''
class Series:
    def __init__(self,title: str,seasons: int,genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.average = 0
    def rate(self,rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)
        self.average = sum(self.ratings) / len(self.ratings)
    def __str__(self):
        return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{len(self.ratings)} ratings, average {self.average:.1f} points"
def minimum_grade(rating: float, series_list: list):
    new_list = []
    for s in series_list:
        if s.average >= rating:
            new_list.append(s)
    return new_list
def includes_genre(genre: str, series_list: list):
    new_list = []
    for s in series_list:
        if genre in s.genres:
            new_list.append(s)
    return new_list

s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)
s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)
s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)
print(s1)
series_list = [s1, s2, s3]
print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)


