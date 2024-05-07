def solution(dec) :
    stack = []    # 이진수를 담을 리스트
    shr = dec; rmd = 0
    
    while shr != 0 :
        rmd = shr % 2
        shr //= 2                   # // : 몫 연산자
        stack.append(str(rmd))      # 나머지(rmd)를 str형으로 변환시켜 추가해야 binary에 str형으로 pop() 가능

    binary = ""
    while stack :
        binary += stack.pop()

    return binary


print(solution(10))
print(solution(27))
print(solution(12345))