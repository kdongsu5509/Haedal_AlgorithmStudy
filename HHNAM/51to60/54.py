def solution(s):
  counts = [0] * 26  

  for c in s:
    counts[ord(c) - ord("a")] += 1

  sorted_str = ""
  for i in range(26):
    sorted_str += chr(i + ord("a")) * counts[i]

  return sorted_str
  
  
# print(solution('hello')) 
# print(solution('algorithm'))