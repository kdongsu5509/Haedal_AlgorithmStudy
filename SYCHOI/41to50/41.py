def solution(graph, source) :
    num_vertices = len(graph)       # 그래프의 노드 수

    distance = [float("inf")] * num_vertices    # 거리 배열 초기화
    distance[source] = 0

    predecessor = [None] * num_vertices         # 직전 경로 배열 초기화

    for temp in range(num_vertices - 1) :                   # 간선 수 만큼 반복하여 최단 경로 갱신
        for u in range(num_vertices) :
            for v, weight in graph[u] :
                if distance[u] + weight < distance[v] :     # 현재 노드 u를 거쳐서 노드 v로 가는 겨올의 거리가 기존에 저장된 노드 v까지의 거리보다 짧은 경우
                    distance[v] = distance[u] + weight      # 최단 거리 갱신
                    predecessor[v] = u                      # 직전 경로 업데이트
    
    for u in range(num_vertices) :                          # 음의 가중치 순회 체크
        for v, weight in graph[u] :
            if distance[u] + weight < distance[v] :         # 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가 기존에 저장된 노드 v까지의 거리보다 짧은 경우
                return [-1]                                 # 음의 가중치 순회 발견 : -1 반환
    
    return [distance, predecessor]


#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]], 0))
print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]], 0))