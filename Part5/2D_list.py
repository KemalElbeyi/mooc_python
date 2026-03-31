def sum_of_column(my_matrix, column_no: int):
    # go through each row and select the item at the chosen position
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]

    return column_sum

def column(my_matrix, column_no: int):
    my_list=[]
    for row in my_matrix:
        my_list.append(row[column_no])

    return my_list

def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        if element in row:
            count += row.count(element)
    return count


m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]


print(sum_of_column(m, 2))
print(column(m, 0))
print(count_matching_elements(m, 2))