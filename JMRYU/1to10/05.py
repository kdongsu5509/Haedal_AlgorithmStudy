def solution(arr1, arr2):

    result = [[sum(a * b for a, b in zip(row, col)) 
               for col in arr2_transposed = list(zip(*arr2))] for row in arr1]

    return result

