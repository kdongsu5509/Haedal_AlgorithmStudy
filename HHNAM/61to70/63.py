def multiply_matrices(matrix1, matrix2):
  result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  for i in range(3):
    for j in range(3):
      for k in range(3):
        result[i][j] += matrix1[i][k] * matrix2[k][j]

  return result

def transpose_matrix(matrix):
  result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  for i in range(3):
    for j in range(3):
      result[j][i] = matrix[i][j]

  return result

def solution(matrix1, matrix2):
  multiplied = multiply_matrices(matrix1, matrix2)

  transposed = transpose_matrix(multiplied)
  return transposed

'''
print(solution(
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
],

[
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]))
'''