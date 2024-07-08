def solution(N, stage):
    challenger = [0] * (N + 2)
    all_players = len(stage)

    for a in stage:
        if a <= N:
            challenger[a] += 1

    fail = [0] * (N + 1)
    for i in range(1, N + 1):
        if all_players == 0:
            fail[i] = 0
        else:
            fail[i] = challenger[i] / all_players
            all_players -= challenger[i]

    result = sorted(range(1, N + 1), key=lambda x: fail[x], reverse=True)
    
    return result
