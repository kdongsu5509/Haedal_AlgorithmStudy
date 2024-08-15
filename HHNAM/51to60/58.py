def solution(array, commands):
  answer = []
  for cmd in commands:
    i, j, k = cmd
    sliced_arr = array[i - 1 : j]  
    sorted_arr = sorted(sliced_arr)  
    answer.append(sorted_arr[k - 1])  
  return answer