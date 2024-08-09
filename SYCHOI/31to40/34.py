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
        
    # 책의 예시(더 쉬운 방법)
    # num_set = set(nums)             # 폰켓몬 종류의 번호를 중복이 없는 집합으로 생성
    # n = len(nums)
    # k = n // 2                      # k는 최대 뽑을 수 있는 폰켓몬의 수
    # return min(k, len(num_set))     # 폰켓몬 종류 수(num_set)와 뽑을 수 있는 폰켓몬의 수(k) 중에 작은 값을 리턴
        
    return cnt


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([3, 1, 2, 3]))
# print(solution([3, 3, 3, 2, 2, 4]))
# print(solution([3, 3, 3, 2, 2, 2]))