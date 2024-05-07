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
            


print(solution('(())()'))
print(solution('((())()'))