def solution(lst) :
    a = list(set(lst))
    a.sort(reverse = True)
    return a 