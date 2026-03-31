list1 = [1, 2, 3, 4]
list2 = list1

list1[0] = 10
list2[1] = 20

print(list1)
print(list2)

print("----------------------------------------")

list1 = [1,2,3,4]
list2 = list1[:]
list1[0] = 10
list2[0] = 20
print(list1)
print(list2)
print(id(list1))
print(id(list2))

print("----------------------------------------")

my_list = [1,2,3,4]
my_list[1:3] = [5,6]
print(my_list)

print("----------------------------------------")

def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)
    my_list = new_list

numbers = [1, 2, 3]
print("in the beginning:", numbers)
augment_all(numbers)
print("after the function is executed:", numbers)

def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)
    my_list[:] = new_list

numbers = [1, 2, 3]
print("in the beginning:", numbers)
augment_all(numbers)
print("after the function is executed:", numbers)

print("----------------------------------------")

def double_items(numbers: list):
    new_numbers = []
    for i in range(len(numbers)):
        new_numbers.append(numbers[i] * 2)
    return new_numbers

numbers = [2, 4, 5, 3, 11, -4]
numbers_doubled = double_items(numbers)
print("original:", numbers)
print("doubled:", numbers_doubled)

print("----------------------------------------")

def remove_smallest(numbers: list):
    min = numbers[0]
    for item in numbers:
        if item < min:
            min = item
    numbers.remove(min)

numbers = [2, 4, 6, 1, 3, 5]
remove_smallest(numbers)
print(numbers)

print("----------------------------------------")

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
def print_sudoku(sudoku: list):
    new_list = []
    for row in sudoku:
        new_row = []
        for num in row:
            if num == 0:
                new_row.append("_")
            else:
                new_row.append(num)
        new_list.append(new_row)
    sudoku[:] = new_list
    for row in sudoku:
        for item in row:
            print(item, end=" ")
        print()
def add_number(sudoku: list, number1: int, number2: int, number3: int):
    sudoku[number1][number2] = number3
    return sudoku

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)

print("----------------------------------------")

def transpose(matrix: list):
    new_matrix = []
    for row in matrix:
        copy_row=row[:]
        new_matrix.append(copy_row)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

def transpose2(matrix: list):
    new_matrix = []
    for i in range(len(matrix)):
        row=[]
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = transpose(matrix)
print(new_matrix)
new_matrix = transpose2(matrix)
print(new_matrix)

print("----------------------------------------")

game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
def play_turn(game_board: list, x: int, y: int, piece: str):
    check = True
    if game_board[x][y] or x<0 or y<0 or x>2 or y>2:
        check = False
    else:
        game_board[x][y] = piece
    return check

print(play_turn(game_board, 2, 0, "X"))
print(play_turn(game_board, 2, 0, "X"))
print(game_board)