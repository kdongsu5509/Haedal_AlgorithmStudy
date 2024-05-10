from collections import deque

def solution(N,K):
    #1~N까지 덱에추가
    queue=deque(range(1,N+1))
    while len(queue)>1:
        for _ in range(K-1):
            #앞에꺼 빼서 뒤에 추가
            queue.append(queue.popleft())
            queue.popleft()
    return queue[0]
