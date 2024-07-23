def solution(n, k, cmd) :
    lst = [i for i in range(n)]
    stack = []
    
    for x in cmd :
        idx = x.split()
        if idx[0] == "D" :
            k = k + int(idx[1])
        elif idx[0] == "U" :
            k = k - int(idx[1])
        elif idx[0] == "C" :
            stack.append((k, lst[k]))
            del(lst[k])
            if len(lst) == k :
                k = k - 1
        elif idx[0] == "Z" :
            l, element = stack.pop()
            lst.insert(l, element)
            if l < k :
                k += 1

    result = ''
    j = 0
    for i in range(n) :
        if i == lst[j] :
            result += "O"
            j += 1
        else :
            result += "X"
    
    return result

#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))