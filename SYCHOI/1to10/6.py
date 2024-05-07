def solution(N, stages) : 
    res = {}                            # 왜 딕셔너리..?
    arv = 0; nClr = 0
    for i in range(1, N+1) :            # 1단계부터 마지막 단계까지 순회
        for j in range(len(stages)) :   # 각 플레이어들의 단계
            if stages[j] >= i :         # 플레이어들의 단계가 i보다 크면 도달했다는 뜻
                arv += 1
            if stages[j] == i :         # 플레이어들의 단계가 i와 같으면 도달했지만 클리어하지 못했다는 뜻
                nClr += 1
        res[i] = nClr/arv
        arv = 0; nClr = 0

    nRes = sorted(res, key=lambda x : res[x], reverse=True)     # sorted() 함수는 바로 출력하거나 다른 변수에 저장하지 않으면 저장X
    return nRes

# 예제
#def solution(N, stages) :
    challenger = [0] * (N + 2)      # 모든 stage를 클리어한 사람은 N+1번째에 있으므로 N+2만큼 선언
    for stage in stages :
        challenger[stage] += 1      # 해당 stage의 도전자들의 수
    
    fails = {}                      # 내림차순한 원소의 인덱스를 출력해야하므로 딕셔너리로 선언
    total = len(stages)
    
    for i in range(1, N+1) :                        # range는 stage를 의미
        if challenger[i] == 0 :                     # 현재 stage(i)의 도전자가 없으면
            fails[i] = 0                            # 실패율 = 0
        else :                                      # 현재 stage(i)의 도전자가 있으면
            fails[i] = challenger[i] / total        # 실패율 = 도전자 수 / stage를 진행한 사람 수
            total -= challenger[i]                  # stage 진행한 사람 수 - 도전자 수 => 다음 stage 진행한 사람 수

    result = sorted(fails, key=lambda x : fails[x], reverse=True)
    return result


print(solution(5, [2,1,2,6,2,4,3,3]))  # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4]))        # [4,1,2,3]