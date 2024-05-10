def solution(arr1, arr2) :
    resA = [[0 for a in range(len(arr2[0]))] for b in range(len(arr1))]     # 첫번째 range가 열 개수, 두번째 range가 행 개수
    sum = 0
    for i in range(len(arr1)) :         # 첫번째 행렬의 행 개수
        for j in range(len(arr2[0])) :  # 두번째 행렬의 열 개수
            for k in range(len(arr2)) : # 혹은 arr1[0] (첫번째 행렬의 열, 두번째 행렬의 행)
                resA[i][j] += arr1[i][k] * arr2[k][j]
    return resA


# r1, c1 = len(arr1), len(arr1[0])
# r2, c2 = len(arr2), len(arr2[0])
# r1은 첫번째 행렬의 행 개수, c1은 첫번째 행렬의 열 개수
# r2는 두번째 행렬의 행 개수, c2는 두번째 행렬의 열 개수
# 행렬의 곱 결과 행 개수는 r1, 열 개수는 c2가 됨

# print(solution([[1,4],[3,2],[4,1]], [[3,3],[3,3]]))
# print(solution([[2,3,2],[4,2,4],[3,1,4]], [[5,4,3],[2,4,1],[3,1,1]]))