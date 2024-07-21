def solution(s):
    stack = []

    for v in s:
        if v == "(":
            stack.append(v)
        elif v == ")":
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True