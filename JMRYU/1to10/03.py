def solution(number):
    a = []
    for s in range(len(number)):
       for p in range (s +1, len(number)):
           a.append(number[s] + number[p])
    a = sorted(set(a))
    return a