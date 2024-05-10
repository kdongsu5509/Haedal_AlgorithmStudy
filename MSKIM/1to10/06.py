def solution(N,stages):
    ppl=[0]*(N+2)
    for stages in stages:
        ppl[stage]+=1

    #{stage,실패율} 쌍으로 저장
    fails={}
    #전체인원 num= len(stages)에서 시작
    num=len(stages)

    #stage가 N개 이므로 stage별로 실패율 계산
    for i in range(1,N+1):
        if ppl[i]==0:
            fails[i]=0
        else:
            fails[i]=ppl[i]/num
            num-=ppl[i]

    result=sorted(fails,key=lambda x: fails[x],reverse=True)

    return result