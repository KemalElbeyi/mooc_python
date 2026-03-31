import numpy as np

# Verilen matris
matrix = [
    [9, 4],
    [6, 3],
    [5, 8]
]

# Matrisin boyutlarını al
rows = len(matrix)
cols = len(matrix[0])

# Benzersiz sayıları çıkar ve sıralanmış bir liste oluştur
unique_numbers = sorted(list(set(sum(matrix, []))))

# Komşuluk matrisini oluşturmak için boş bir matris oluştur
adj_matrix = np.zeros((len(unique_numbers), len(unique_numbers)), dtype=int)

# Sayıların sıralı haliyle indeksini tutmak için bir sözlük oluştur
number_to_index = {number: index for index, number in enumerate(unique_numbers)}

# Komşuluk matrisini doldur
for i in range(rows):
    for j in range(cols):
        current = matrix[i][j]
        if i > 0:  # Yukarıdaki komşu
            adj_matrix[number_to_index[current]][number_to_index[matrix[i-1][j]]] = 1
        if i < rows - 1:  # Aşağıdaki komşu
            adj_matrix[number_to_index[current]][number_to_index[matrix[i+1][j]]] = 1
        if j > 0:  # Soldaki komşu
            adj_matrix[number_to_index[current]][number_to_index[matrix[i][j-1]]] = 1
        if j < cols - 1:  # Sağdaki komşu
            adj_matrix[number_to_index[current]][number_to_index[matrix[i][j+1]]] = 1

# Çıktıyı yazdır
print("   ", end="")
for number in unique_numbers:
    print(f"{number:3}", end="")
print()

for i, number in enumerate(unique_numbers):
    print(f"{number:3}", end="")
    for j in range(len(unique_numbers)):
        print(f"{adj_matrix[i][j]:3}", end="")
    print()

