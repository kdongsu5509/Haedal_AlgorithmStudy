def dfs(computers, visited, node) :
    visited[node] = True        # 현재 노드 방문 처리
    for idx, connected in enumerate(computers[node]) :
        if connected and not visited[idx] :         # 연결되어 있으며 방문하지 않은 노드라면
            dfs(computers, visited, idx)            # 해당 노드 방문

def solution(n, computers) :
    answer = 0
    visited = [False] * n                   # 방문 여부 저장하는 리스트
    for i in range(n) :
        if not visited[i] :                 # 아직 방문하지 않은 노드라면
            dfs(computers, visited, i)      # 해당 노드를 시작으로 깊이 우선 탐색 진행
            answer += 1                     # dfs로 연결된 노드들을 모두 방문하면서 네트워크 개수 증가

    return answer

#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))