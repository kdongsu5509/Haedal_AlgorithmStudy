from collections import deque

def solution(progresses, speeds):
    pr = deque(progresses)
    sp = deque(speeds)
    answer = []
    while(len(pr) != 0):
        cnt = 0
        for x in range(len(pr)):
            pr[x] += sp[x]
        print(pr)
        if(len(pr) != 0 and pr[0] >= 100):
            while(len(pr) != 0 and pr[0] >= 100):
                cnt += 1
                pr.popleft()
                sp.popleft()
            answer.append(cnt)
    return answer