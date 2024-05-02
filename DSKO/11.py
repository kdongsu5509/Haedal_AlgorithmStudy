def solution(s):
    #s is input of the string.
    stack = []
    for temp in s:
        #if stack's length is 0 then result is 1 or 0.
        #appending element to stack.
        if len(stack) == 0 or stack[-1] != temp:
            stack.append(temp)
            #after that let's do pop!
        elif len(stack) != 0 and stack[-1] == temp:
            stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer