def solution(a):
    pattern = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    score = [] * 3
    for b, an in enumerate(a):
        for c, p in enumerate(pattern):
            if an == p[b % len(p)]:
                score[c] += 1
    maxs = max(score)
    ms = []
    for b, s in enumerate(score):
        if s == maxs:
            ms.append(b+1)
    return ms 