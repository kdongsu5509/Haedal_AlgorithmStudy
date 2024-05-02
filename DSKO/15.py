from collections import deque

def solution(n, k):
    queue = deque(range(1, n+1))

    while len(queue) > 1:
        for _ in range(k - 1):
            queue.append(queue.popleft())

            queue.popleft()
    return queue[0]

print(solution(5,2))