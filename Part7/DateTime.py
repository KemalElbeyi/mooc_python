from datetime import datetime,timedelta
def cal_agebydays(day: int,month: int,year: int):
    birthday = datetime(year,month,day)
    time_now = datetime.now()
    diffrance = time_now - birthday
    print(f"Your age by days: {diffrance.days}")
cal_agebydays(21,4,2025)

print("----------------------------------")

def is_it_valid(pic: str):
    dd = int(pic[0:2])
    mm = int(pic[2:4])
    yy = int(pic[4:6])
    x = pic[6]
    if x == '+':
        yil = 1800 + yy
    elif x == '-':
        yil = 1900 + yy
    elif x == 'A':
        yil = 2000 + yy
    else:
        return False

    control = int(pic[:6]+pic[7:10])%31
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if len(pic) != 11:
        return False
    try:
        datetime(yil,mm,dd)
    except ValueError:
        return False
    if pic[10] != control_chars[control]:
        return False
    else:
        return True
print(is_it_valid("310823-9877"))

print("----------------------------------")

start_date_str = input("Starting date: ")
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
start_day = datetime.strptime(start_date_str,"%d.%m.%Y")
minutes = 0
for day in range(days):
    date = start_day + timedelta(days=day)
    date_str = date.strftime("%d.%m.%Y")
    times = input(f"Screen time {date_str}: ")
    tv,computer,mobile = times.split(" ")
    minutes += int(tv)+int(computer)+int(mobile)

print(f"starting day: {start_date_str} \nending day: {(start_day + timedelta(days=days - 1)).strftime("%d.%m.%Y")} \naverage minutes: {minutes/days} \ntotal minutes: {minutes}")

