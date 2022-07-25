from random import shuffle

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

matrix_merge = []
for i in matrix:
    for j in i:
        matrix_merge += [j]

shuffle(matrix_merge)
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = matrix_merge[count]
        count +=1

print(matrix)
