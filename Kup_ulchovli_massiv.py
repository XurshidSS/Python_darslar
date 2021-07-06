# 1-masala
numbersList = [[[1, 2, 3] * 2] * 3] * 2
print(numbersList)

# 2-masala
numbersList = [[1, 2, 3, 4], [0, [1, 2, [4, 5, [10, 11]], 4], 5], 12]
print(numbersList[1][1][2][2][0])

# 3-masala
numbersList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(numbersList[1][1])

# 4-masala
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
a1 = matrix1[0][0] + matrix2[0][0]
a2 = matrix1[0][1] + matrix2[0][1]
a3 = matrix1[1][0] + matrix2[1][0]
a4 = matrix1[1][1] + matrix2[1][1]
matrix = [a1, a2], [a3, a4]
print(matrix)