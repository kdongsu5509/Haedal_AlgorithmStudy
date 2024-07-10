def solution(arr):
    arr_set = list(set(arr))    # 중복값 제거
    arr_set.sort(reverse=True)  # 내림차순 정리
    return arr_set


# print(solution([4, 2, 2, 1, 3, 4]))       
# print(solution([2, 1, 1, 3, 2, 5, 4]))    