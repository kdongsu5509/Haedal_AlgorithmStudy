from heapq import heappush, heappop

def solution(land, height):
  answer = 0
  n = len(land)
  di = [-1, 0, 1, 0]
  dj = [0, 1, 0, -1]
  visited = [[False] * n for _ in range(n)]
  q = []

  heappush(q, [0, 0, 0])  

  while q:
    cost, i, j = heappop(q)
    if not visited[i][j]:
      visited[i][j] = True
      answer += cost
      for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < n and 0 <= nj < n:
          temp_cost = abs(land[i][j] - land[ni][nj])
          if temp_cost > height:
            new_cost = temp_cost
          else:
            new_cost = 0
          heappush(q, [new_cost, ni, nj])

  return answer