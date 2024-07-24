from collections import deque

def isValid(ny, nx, n, m, maps) :
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"
    # 0 <= ny < n : 방문할 y좌표가 지도 내에 있고 / 0 <= nx < m : 방문할 x좌표가 지도 내에 있고
    # 방문할 좌표가 벽이 아니면 return

def append_to_Queue(ny, nx, k, time, visited, q) :
    if not visited[ny][nx][k] :
        visited[ny][nx][k] = True
        q.append((ny, nx, k, time + 1))

def solution(maps) :
    n, m = len(maps), len(maps[0])      # n : maps의 행 개수, m : maps의 열 개수
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]     # [False, False]를 m개의 열 개수만큼, n개의 행 개수만큼 생성
    # Flase for _ in range(2) : [False, False] 생성

    # dy, dx의 인덱스에 따라 상/하/좌/우 구별 가능
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    q = deque()             # q라는 변수에 덱 기능 선언
    endY, endX = -1, -1     # 도착점의 x, y 좌표 넣는 변수. -1로 초기화한다
    
    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == "S" :
                q.append((i, j, 0, 0))      # 덱 q에 시작점 좌표 입력
                visited[i][j][0] = True
            if maps[i][j] == "E" :
                endY, endX = i, j
    
    while q :
        y, x, k, time = q.popleft()

        if y== endY and x == endX and k == 1 :
            return time
        
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i]

            if not isValid(ny, nx, n, m, maps) :
                continue
            
            if maps[ny][nx] == "L" :
                append_to_Queue(ny, nx, 1, time, visited, q)
            else :
                append_to_Queue(ny, nx, k, time, visited, q)

    return -1


    
#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))