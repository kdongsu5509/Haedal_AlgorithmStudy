def solution(n):
  digits = list(str(n))  
  digits.sort(reverse=True)  
  answer = int("".join(digits)) 
  return answer