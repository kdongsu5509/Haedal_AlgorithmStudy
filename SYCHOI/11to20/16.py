import math

def solution(progresses, speeds) :
    result = []
    n = len(progresses)
    cnt = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(n)]    # 각 작업 당 배포일 계산
                                                                            # math.ceil() : 올림
    
    cntN = 0
    max_day = cnt[0]                # 대소 비교 - 가장 첫번째 작업

    for i in range(n) :
        if (cnt[i] <= max_day) :    # 가장 앞 작업보다 작업일이 적으면
            cntN += 1               # 함께 배포(배포 작업 수++)
        else :                      # 가장 앞 작업보다 작업일이 많으면
            max_day = cnt[i]        # 다음 작업부터 대소 비교할 인덱스로 수정
            result.append(cntN)     # 배포 작업 수 리스트 추가
            cntN = 1                # 현재 인덱스 i의 값이 max_day가 되므로 cntN은 1부터 시작 (다음 순회는 i+1)
        
    result.append(cntN)             # 마지막 카운트 추가
    
    return result


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))