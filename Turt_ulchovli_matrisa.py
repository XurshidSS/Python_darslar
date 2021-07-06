# Masala.
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B = A[0] + [A[1][2]] + [A[2][2]] + [A[2][1]] + [A[2][0]] + [A[1][0]] + [A[1][1]]
# print(B)

# Maxsus masala. 3x3 matritsani for yordamida ustunlarini satrga satrlarini
# ustunga almashtiring.

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[[], [], []], [[], [], []], [[], [], []]]
for i in range(3):
    for j in range(3):
        B[i][j] = (A[j][i])
        print(B)

# Masala - 8.
a = [[1, 2], [3, 4]]
for i in a:
    for j in i:
        if j % 2 == 1:
            continue
        print(j)