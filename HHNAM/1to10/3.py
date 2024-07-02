def solution(numbers):
    ret = []                                    # 빈 배열 생성 
    for i in range(len(numbers)):               # 두 수를 선택하는 모든 경우의 수를 반복문으로 구함
        for j in range(i+1, len(numbers)):      # len() : 문자열 길이 반환 함수
            ret.append(numbers[i]+numbers[j])   # 두 수를 더한 결과를 새로운 배열에 추가
    ret = sorted(set(ret))                      # sorted() : 중복된 값을 제거, set() : 오름차순으로 정렬
    
    return ret


# print(solution([2, 1, 3, 4, 1]))  # [2, 3, 4, 5, 6, 7]
# print(solution([5, 0, 2, 7]))     # [2, 5, 7, 9, 12]
