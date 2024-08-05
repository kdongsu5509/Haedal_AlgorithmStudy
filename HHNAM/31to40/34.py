def solution(nums):
  num_set = set(nums) 
  n = len(nums)  
  k = n // 2  
  return min(k, len(num_set))  