def solution(arr, target):
    m = max(arr)
    li = [0] * (m + 1)
    for x in arr:
        li[x] += 1
    for x in arr:
        if x != 0 and target - x != x and li[target - x] > 0:
            return True
    return False

print(solution([1,2,3,4,8], 6))
print(solution([2,3,5,9], 10))