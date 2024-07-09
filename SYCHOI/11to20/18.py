def solution(arr, target) :
    hash_tbl = [0] * (arr[-1] + 1)      # 인덱스는 arr 배열의 숫자, 값은 숫자 존재 여부를 의미.
    result = False                      # arr 배열의 가장 큰 수를 기준으로 hash_tbl 크기를 결정해야 함

    for n in arr :
        hash_tbl[n] = 1                 # arr 배열에 있는 숫자(key)를 기준으로 존재하면 1의 값을 설정한다
        
    for i in range(1, target) :         # 0은 취급하지 않으므로 target - 1까지 순회
        if not(i == target-i) and hash_tbl[i] == 1 and hash_tbl[target-i] == 1 :        # 중복 불가!!
            result = True

    return result


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([1, 2, 3, 4, 8], 6))
# print(solution([2, 3, 5, 9], 10))