def solution(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2
    stack.reverse()
    return ''.join(stack)
    
    
# print(solution(10)) 
# print(solution(27))
# print(solution(12345))