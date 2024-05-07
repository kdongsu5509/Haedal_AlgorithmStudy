def solution(arr):
    uni = list(set(arr))
    uni.sort(reverse=True)
    return uni