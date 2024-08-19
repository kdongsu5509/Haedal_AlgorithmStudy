def solution(arr, n):
  def rotate_90(arr):
    n = len(arr)

    rotated_arr = [[0] * n for _ in range(n)]

    for i in range(n):
      for j in range(n):
        rotated_arr[j][n - i - 1] = arr[i][j]

    return rotated_arr

  rotated_arr = arr.copy()

  for _ in range(n):
    rotated_arr = rotate_90(rotated_arr)

  return rotated_arr

# print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1))