#O(N)알고리즘 / 스택사용
#이해가 안되요 ㅠ 난 큐쓸래
def solution(prices):
    n=len(prices)
    answer=[0]*n

    stack=[0]
    for i in range(1,n):
        while stack and prices[i]<prices[stack[-1]]:
            j=stack.pop()
            answer[j]=i-j
        stack.append(i)

    while stack:
        j=stack.pop()
        answer[j]=n-1-j
    return answer

#O(N)알고리즘 / 큐사용
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer

#O(N^2)알고리즘
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer