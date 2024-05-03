import sys
input=sys.stdin.readline

def solution(arr):
    a=list(set(arr))
    a.sort(reverse=True)
    return a

n=list(map(int,input().split()))
print(solution(n))