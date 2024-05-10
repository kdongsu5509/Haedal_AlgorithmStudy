def solution(a):
    pattern = [
        [1,2,3,4,5],
        [2,1,2,3,2],
        [3,3,1,1,2]
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