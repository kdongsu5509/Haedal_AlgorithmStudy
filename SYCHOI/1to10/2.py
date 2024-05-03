def solution(arr) :
    arr = list(set(arr))        # set : 집합 생성 함수, 중복값 제거, 튜플로 반환
    arr.sort(reverse=True)      # newArr = sorted(arr, reverse = True)
    return arr

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([4, 2, 2, 1, 3, 4])) # 반환값 : [4, 3, 2, 1]
# print(solution([2, 1, 1, 3, 2, 5, 4])) # 반환값 : [5, 4, 3, 2, 1]

# set함수 시간 복잡도 O(N)