def solution(s) :
    stack = []

    for x in s :
        if x == '(' :
            stack.append(x)
        elif x == ')' :
            if not stack :      # stack이 비어있으면
                return False
            else :
                stack.pop()

    if stack :                  # stack에 원소가 있으면
        return False            # if len(stack) == 0 을 사용하는 것은 권장하지 않음
    else :
        return True
            


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution('(())()'))
# print(solution('((())()'))