def solution(N, K) :
    queue = []
    for i in range(N) :
        queue.append(i+1)

    while(queue) :              # queue에 요소가 있는 동안
        for x in range(K-1) :   # K-1번째 전까지의 요소들을 뒤로 보내기(원형 큐로 생각)
            idx = queue.pop(0)
            queue.append(idx)
        answer = queue.pop(0)   # K번째 요소 pop(마지막엔 리턴해야하므로 변수에 저장)

    return answer


print(solution(5, 2))