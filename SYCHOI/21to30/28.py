def solution(N, A, B) :
    result = 1
    while (1) :
        A = int((A + 1) / 2)        # A = (A + 1) // 2
        B = int((B + 1) / 2)        # B = (B + 1) // 2
        if A == B : 
            break
        result += 1

    return result


#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(8, 4, 7))