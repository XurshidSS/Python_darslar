# # Masala. 2x2 matrisa
# A1 = [[1, 2], [3, 4]]
# A2 = [[5, 6], [7, 8]]
# B = [[[], []], [[], []]]
# for i in range(2):
#     for j in range(2):
#         B[i][j] = A1[i][j] + A2[i][j]
#
# print(B)
#
# # Masala. 3x3 matrisa
#
# matrix = [[[], [], []], [[], [], []], [[], [], []]]
#
# for i in range(3):
#     for j in range(3):
#         matrix[i][j] = int(input(f"matrix[{i}][{j}] = "))
# print(matrix)

# Masala.

# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for matrix in matrix1:
#     for index in matrix:
#         print(index)

# Masala. Massiv elementlarini bitta massivga birlashtirish.
# 1-usul.
matrix = [[1, 2], [3, 4]]
matrix1 = matrix[0] + matrix[1]
print(matrix1)

# 2-usul.
c = []
for matrix1 in matrix:
    for matrix2 in matrix1:
        c.append(matrix2)
print(c)

# 3-usul.
c = matrix[0] + matrix[1]
print(c)