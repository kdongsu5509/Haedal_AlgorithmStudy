def solution(prices):
    #1. stack과 time list 선언
    stack = []
    time = [0] * len(prices)
    
    #2. stack에 넣기 시작하자.
    #a. stack은 2차원 배열임.
    #b. idx에 주의할 것.
    idx = 0
    for idx in range(len(prices)):
        if not stack or stack[-1][0] <= prices[idx]:
            stack.append([prices[idx],idx])
        elif stack and stack[-1][0] > prices[idx]:
            while(stack and stack[-1][0] > prices[idx]):
                temp = stack.pop()
                out_value, out_idx = temp
                time[out_idx] = idx - out_idx
            stack.append([prices[idx], idx])
    # print(stack)
    while(stack):
        temp = stack.pop()
        out_value, out_idx = temp
        time[out_idx] = idx - out_idx
    return time