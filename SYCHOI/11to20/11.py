def solution(s) :
    stack = []

    for x in s :
        if stack and x == stack[-1] :       # if stack 조건을 넣지 않으면 <list index out of range> 에러가 뜸
            stack.pop()                     # stack[-1]은 stack의 top 요소를 가리킴, 즉 가장 최근에 추가한 데이터
        else :
            stack.append(x)
    
    if not stack :
        return 1
    else :
        return 0
        

#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution("baabaa"))
# print(solution("cdcd"))