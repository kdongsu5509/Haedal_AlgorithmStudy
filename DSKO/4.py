def solution(answers):
    answer = len(answers)
    #1번 수포자
    first = []
    for x in range(10000):
        will_in = (x+1)%5
        if will_in == 0:
            will_in = 5
        first.append(will_in)
        
    #2번 수포자
    second = []
    integer = 1
    for x in range(5000):
        second.append(2)
        will_in = (integer%5)
        if will_in == 0:
            will_in = 5
        if will_in == 2:
            will_in = 3
            integer += 1
        second.append(will_in)
        integer += 1
    print(second)
    #3번 수포자.
    third = []
    order = [3,1,2,4,5]
    for x in range(5000):
        idx=x % 5
        third.append(order[idx])
        third.append(order[idx])
        # third.append(idx)

    answer = []
    f = 0
    s = 0
    t = 0
    index = 0
    for answer in answers:
        if first[index] == answer:
            f+=1
        if second[index] == answer:
            s+=1
        if third[index] == answer:
            t+=1
        index+=1
    print(f,s,t)
    li = [f,s,t]
    high = max(li)
    best = []

    if(f == high):
        best.append(1)
    if(s == high):
        best.append(2)
    if(t == high):
        best.append(3)
    return sorted(best)