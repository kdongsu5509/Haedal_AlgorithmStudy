from collections import deque

def solution(N, K):
  que = deque(range(1, N+1))

  while len(que)>1:
    for _ in range(K -1):
      que.append(que.popleft())

      que.popleft()
    return que[0]
print(solution(5,2)) 