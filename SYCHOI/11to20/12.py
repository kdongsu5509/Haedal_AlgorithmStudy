def solution(prices) :
    stack = []          # 각 주식의 인덱스를 저장할 STACK
    result = [0] * len(prices)       # 각 주식의 상승한 시점 길이를 저장할 STACK
    stack.append(0)

    for i in range(1, len(prices)) :
        if prices[i] >= prices[stack[-1]] :           # 현재 주식보다 이전 주식의 가격이 같거나 낮으면(주식이 상승하면)
            stack.append(i)
        else : # prices[i] < prices[stack[-1]]          현재 주식보다 이전 주식의 가격이 높으면(주식이 하락하면)
            idx = stack.pop()
            result[idx] = i - idx
            stack.append(i)
    
    fin = stack.pop()           # 마지막 시점
    idx = fin                   # stack 안에 남은 idx 값들을 담을 변수
    while(stack) :              # stack 안에 인덱스가 남아있다면
        result[idx] = fin - idx
        idx = stack.pop()
    result[idx] = fin - idx     # 마지막 pop으로 인해 마지막 idx에 대한 값이 설정되지 않는 것을 while문 밖에서 설정

    return result


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([1, 2, 3, 2, 3]))            # [4, 3, 1, 1, 0]