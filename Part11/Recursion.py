def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        numbers.append(numbers[-1]+1)
        add_numbers_to_list(numbers)

numbers = [1,3,4,5,10,11]
add_numbers_to_list(numbers)
print(numbers)

print("------------------------------")

def sum_digit(num: int):
    if num < 10:
        return num
    top = num % 10
    return top + sum_digit(num//10)
print(sum_digit(463))

print("------------------------------")

def recursive_sum(num: int):
    if num < 1:
        return num
    return num + recursive_sum(num - 1)
print(recursive_sum(5))
print(recursive_sum(10))

print("------------------------------")

def balanced_brackets(my_string: str):
    new_string = "".join(char for char in my_string if char in "()[]")
    if len(new_string) == 0:
        return True
    if (new_string[0] in "(" and new_string[-1] in ")") or (new_string[0] == "[" and new_string[-1] == "]"):
        return balanced_brackets(new_string[1:-1])
    else:
        return False
print(balanced_brackets("((()))"))
print(balanced_brackets("([([])])"))
print(balanced_brackets("(python version [3.7]) please use this one!"))
print(balanced_brackets("([bad egg)]"))

print("------------------------------")

def basamak_topla(s1: int, s2: int, elde=0):
    if s1==0 and s2==0 and elde==0:
        return 0
    s1_son_bas = s1 % 10
    s2_son_bas = s2 % 10
    toplam = s1_son_bas + s2_son_bas + elde
    basamak = toplam % 10
    yeni_elde = toplam // 10

    yeni_basamak = basamak_topla(s1 // 10,s2 // 10,yeni_elde)
    return yeni_basamak * 10 + basamak
print(basamak_topla(99,98))

