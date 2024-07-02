import math

def solution(progresses, speeds) :
    result = []
    n = len(progresses)
    cnt = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(n)]    # 각 작업 당 배포일 계산
                                                                            # math.ceil() : 올림
    
    cntN = 0
    max_day = cnt[0]

    for i in range(n) :
        if (cnt[i] <= max_day) :
            cntN += 1
        else :
            max_day = cnt[i]
            result.append(cntN)
            cntN = 1                # 현재 인덱스 i의 값이 max_day가 되므로 cntN은 1부터 시작 (다음 순회는 i+1)
        
    result.append(cntN)             # 마지막 카운트 추가

    return result


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))