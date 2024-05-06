def solution(numbers) :
    result = []
    for i in range(len(numbers)) :              # 0부터 len(numbers)-1까지
        for j in range(i+1, len(numbers)) :     # i+1부터 lne(numbers)-1까지
            result.append(numbers[i]+numbers[j])
    result = list(set(result))                  # 중복 제거(집합 생성)
    return result


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([2, 1, 3, 4, 1])) # 반환값 : [2, 3, 4, 5, 6, 7]
# print(solution([5, 0, 2, 7])) # 반환값 : [2, 5, 7, 9, 12]