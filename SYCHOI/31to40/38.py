from collections import defaultdict

def solution(graph, start) :
    adj_list = defaultdict(list)        # 그래프를 인접 리스트로 변환
    for u, v in graph :
        adj_list[u].append(v)

    # DFS 탐색 함수
    def dfs (node, visited, result) :
        visited.add(node)       # 현재 노드를 방문한 노드들의 집합에 추가
        result.append(node)     # 현재 노드를 결과 리스트에 추가

        for neighbor in adj_list.get(node, []) :        # 현재 노드와 인접한 노드 순회 
            if neighbor not in visited :                # 아직 방문하지 않은 노드라면
                dfs(neighbor, visited, result)          # dfs 탐색

    # DFS를 순회한 결과 반환
    visited = set()
    result = []
    dfs(start, visited, result)     # 시작 노드에서 깊이 우선 탐색 시작

    return result



#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'))
print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'))