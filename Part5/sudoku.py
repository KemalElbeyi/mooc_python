sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

def row_correct(sudoku: list, row_no: int):
    row=sudoku[row_no]
    for var in row:
        if var>0 and row.count(var)>1:
            return False
        else:
            return True

print(row_correct(sudoku, 1))

def column_correct(sudoku: list, column_no: int):
    column=[]
    for row in sudoku:
        column.append(row[column_no])
    column_control=True
    for var in column:
        if var>0 and column.count(var)>1:
            column_control=False
            break
    return column_control

print(column_correct(sudoku, 2))

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            block.append(sudoku[i][j])
    block_control=True
    for var in block:
        if block.count(var)>1 and var>0:
            block_control=False
            break
    return block_control

print(block_correct(sudoku, 0, 0))

def grid_correct(sudoku: list):
    #row control
    for i in range(len(sudoku)):
        if row_correct(sudoku,i)==False:
            return False
    #column control
    for i in range(len(sudoku)):
        if column_correct(sudoku,i)==False:
            return False
    #block control
    for i in range(0,7,3):
        for j in range(0,7,3):
            if block_correct(sudoku,i,j)==False:
                return False
    return True

print(grid_correct(sudoku))