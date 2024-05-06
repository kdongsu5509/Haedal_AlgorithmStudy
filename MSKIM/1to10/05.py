

def soluiton(arr1,arr2):
    a,b=len(arr1),len(arr1[0])
    c,d=len(arr2),len(arr2[0])

    matrix=[[0]*d for _ in range(a)]

    for i in range(a):
        for j in range(d):
            for k in range(c):
                matrix[i][j]+=arr1[i][k]*arr2[k][j]
    return matrix