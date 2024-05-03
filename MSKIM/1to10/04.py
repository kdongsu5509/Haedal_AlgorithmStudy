import sys
input=sys.stdin.readline

def solution(arr):
    patterns=[
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    scores=[0]*3

    for i,answer in enumerate(arr):
        for j,pattern in enumerate(patterns):
            if answer==pattern[i%len(pattern)]:
                scores[j]+=1
    max_score=max(scores)
    answer=[]
    for i,score in enumerate(scores):
        if score==max_score:
            answer.append(i+1)
    return answer

n=list(map(int,input().split()))
print(solution(n))
