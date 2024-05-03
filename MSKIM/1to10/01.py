import sys
input=sys.stdin.readline

def solution(arr):
    arr.sort()
    return arr

n=list(map(int,input().split()))
print(solution(n))
