def solution(arr1, arr2):
  merged = []  
  i, j = 0, 0  

  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      merged.append(arr1[i])
      i += 1
    else:
      merged.append(arr2[j])
      j += 1

  while i < len(arr1):
    merged.append(arr1[i])
    i += 1
  while j < len(arr2):
    merged.append(arr2[j])
    j += 1

  return merged

  
# print(solution([1, 3, 5], [2, 4, 6])) 
# print(solution([1, 2, 3], [4, 5, 6])) 