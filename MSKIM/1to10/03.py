import sys
input=sys.stdin.readline

def solution(arr):
    a=[]
    num=len(arr)
    for i in range(num):
        for j in range(i+1,num):
            a.append(arr[i]+arr[j])

    a=sorted(set(a))
    return a

n=list(map(int,input().split()))
print(solution(n))