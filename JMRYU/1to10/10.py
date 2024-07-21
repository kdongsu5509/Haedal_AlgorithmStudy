def is_valid(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching():
            stack.append(char)
        elif char in matching():
            if stack == [] or matching[char] != stack.pop():
                return False
    return stack == []

def solution(s):
    ans = 0 
    n = len(s)
    
    for i in range(n):
        rotated_s = s[i:] + s[:i]  
        if is_valid(rotated_s):
            ans += 1
    return ans
