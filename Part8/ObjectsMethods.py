def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1 = (person1["result1"]+person1["result2"]+person1["result3"])/3
    avg2 = (person2["result1"]+person2["result2"]+person2["result3"])/3
    avg3 = (person3["result1"]+person3["result2"]+person3["result3"])/3
    smallest = min((avg1,person1),(avg2,person2),(avg3,person3))
    return smallest[1]
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))

print("-----------------------------------")

def row_sums(my_matrix: list):
    for row in my_matrix:
        row.append(sum(row))
my_matrix = [[1, 2], [3, 4]]
row_sums(my_matrix)
print(my_matrix)