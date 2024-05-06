def solution(num):
    stack = []
    while num > 0:
        a = num % 2
        stack.append(str(a))
        num //= 2
    string = "".join(stack[::-1])
    return string

