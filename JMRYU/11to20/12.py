def solution(prices):
    stack = []
    result = [0] * len(prices)   

    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()  
            result[idx] = i - idx  
        stack.append(i)  

    while stack:
        idx = stack.pop()
        result[idx] = len(prices) - 1 - idx 

    return result
 