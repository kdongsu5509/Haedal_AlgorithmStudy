import heapq

def solution(N, road, K) :
    graph = [[] for _ in range(N + 1)]      # 각 노드에 연결된 간선들을 저장할 리스트
    distances = [float("inf")] * (N + 1)    # 출발점에서 각 노드까지의 최단 거리를 저장할 리스트
    distances[1] = 0                        # 출발점은 0으로 초기화

    for a, b, cost in road :                # 그래프 구성
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    # 다익스트라 알고리즘 시작
    heap = []
    heapq.heappush(heap, (0, 1))        # 출발점을 heap에 추가
    while heap :
        dist, node = heapq.heappop(heap)

        for next_node, next_dist in graph[node] :           # 인접한 노드들의 최단 거리를 갱신하고 heap에 추가
            cost = dist + next_dist
            if cost < distances[next_node] :
                distances[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

    # distances 리스트에서 K 이하인 값의 개수를 구하여 반환
    return sum(1 for dist in distances if dist <= K)

#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))