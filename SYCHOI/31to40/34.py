def solution(nums) :    # nums : 폰켓몬의 종류 번호가 담긴 1차원 배열
    halfN = len(nums) // 2      # int(len(nums) / 2)
    idx = [0 for i in range(max(nums) + 1)]

    cnt = 0
    for n in nums :
        if idx[n] == 0 :
            cnt += 1
            idx[n] = 1

        if halfN == cnt :
            return halfN
        
    return cnt


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([3, 1, 2, 3]))
# print(solution([3, 3, 3, 2, 2, 4]))
# print(solution([3, 3, 3, 2, 2, 2]))