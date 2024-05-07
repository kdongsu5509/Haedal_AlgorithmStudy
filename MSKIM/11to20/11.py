def solution(s):
    stack=[]
    for a in s:
        if stack and stack[-1]==a:
            stack.pop()
        else:
            stack.append(a)
    return int(not stack)