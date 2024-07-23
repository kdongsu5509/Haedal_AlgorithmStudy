def solution(dec):
    stack = []

    while dec > 0:
        stack.append(str(dec % 2))
        dec //= 2
   
    bin = "".join(stack[::-1])

    return bin 
