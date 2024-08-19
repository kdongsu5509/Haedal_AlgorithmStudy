def solution(brown, yellow):
  total_size = brown + yellow
  for vertical in range(3, int(total_size**0.5) + 1):
    if total_size % vertical == 0:
      horizontal = (int)(total_size / vertical)  
      if brown == (horizontal + vertical - 2) * 2:
        return [horizontal, vertical]  
  return [] 