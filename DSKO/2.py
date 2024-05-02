def solution(arr):
    arr_set = set(arr)
    setToList = list(arr_set)
    return setToList.sort(reverse=True)