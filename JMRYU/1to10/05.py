def solution(arr1, arr2):

    answer = [[sum(arr1[i][k] * arr2[k][j] for k in range(len(arr1[0]))) for j in range(len(arr2[0]))] for i in range(len(arr1))]

    return answer  
