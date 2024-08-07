def solution(N):
  results = [] 

  def backtrack(sum, selected_nums, start):
    if sum == 10:  
      results.append(selected_nums)
      return

    for i in range(start, N + 1):  
      if sum + i <= 10:  
          backtrack(sum + i, selected_nums + [i], i + 1) 

  backtrack(0, [], 1)  
  return results  


# print(solution(5)) 
# print(solution(2)) 
# print(solution(7))