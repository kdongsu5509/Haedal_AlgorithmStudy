from collections import deque

def solution(maps) :
    move = [[-1, 0], [0, -1], [0, 1], [1, 0]]       # 이동할 수 있는 방향을 나타내는 배열

    n = len(maps)           # 맵의 가로 크기(열 개수)
    m = len(maps[0])        # 맵의 세로 크기(행 개수)

    dist = [[-1] * m for _ in range(n)]             # 거리를 저장하는 배열 dist를 -1로 초기화

    def bfs(start) :                                # bfs 함수 선언
        q = deque([start])                          # deque 선언 후 시작 위치 deque에 추가
        dist[start[0]][start[1]] = 1                    

        while q :
            here = q.popleft()

            for direct in move :                    # 현재 위치에서 이동할 수 있는 모든 방향
                row, column = here[0] + direct[0], here[1] + direct[1]

                if row < 0 or row >= n or column < 0 or column >= m :       # 이동한 위치가 범위를 벗어난 경우 다음 방향으로 넘어감
                    continue

                if maps[row][column] == 0 :                                 # 이동한 위치에 벽이 있는 경우 다음 방향으로 넘어
                    continue
                
                if dist[row][column] == -1 :                                # 이동한 위치가 처음 방문하는 경우, deque에 추가하고 거리 갱신
                    q.append([row, column])
                    dist[row][column] = dist[here[0]][here[1]] + 1

        return dist

    bfs([0, 0])         # 시작 위치에서 bfs() 함수를 호출하여 거리 계산

    return dist[n - 1][m - 1]       # 목적지까지의 거리 반환, 목적지에 도달하지 못한 경우 -1 반환




#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))