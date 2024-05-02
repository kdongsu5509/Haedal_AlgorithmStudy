def solution(participant, completion):
    answer = ''
    d = dict()
    idx = 0
    for x in participant:
        d[x] = idx
        idx += 1
    #	{'leo': 0, 'kiki': 1, 'eden': 2}
    
    #let's make a new list
    li = [0] * len(participant)
    for temp in participant:
        li[d[temp]] += 1 ## transform to list with int
    
    for c in completion:
        li[d[c]] -= 1
    
    for x in range(len(li)):
        if li[x] != 0:
            answer = participant[x]
    return answer