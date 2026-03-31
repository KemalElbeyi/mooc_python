'''with open("Ztext1.txt") as new_file:
    contents = new_file.read()
    print(contents)

print("------------------------------------")

with open("Ztext1.txt") as new_file1:
    count=0
    total_lenght = 0
    for line in new_file1:
        line = line.replace("\n","") #birer satır aralık bırakılmasın diye \n yerine boşluk gelir
        count = count + 1
        print("Satır",count,line)
        length = len(line)
        total_lenght = total_lenght + length
print("Total lenght of lines: ",total_lenght)

print("------------------------------------")

numbers_list = []
with open("Znumber1.txt") as new_file2:
    for num in new_file2:
        numbers_list.append(int(num))
def largest(numbers_list):
    max=numbers_list[0]
    for i in numbers_list:
        if i > max:
            max=i
    return max
print(largest(numbers_list))

print("------------------------------------")

text = "monkey,banana,harpsichord"
words = text.split(",")
print(words)

print("------------------------------------")
'''
not_list = []# bütün sütunların ayrı ayrı ortalamasını al
with open("../Znumber2.csv", encoding="latin-1") as new_file3:
    ort=0
    sum=0
    for line in new_file3:
        line = line.replace("\n","")
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]
        print("Name:", name)
        print("Grades:", grades)
        not_list.append(grades)
print(not_list)

print("------------------------------------")





