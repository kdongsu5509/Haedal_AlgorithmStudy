from collections import deque

def isValid(ny, nx, n, m, maps) :
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"
    # 0 <= ny < n : 방문할 y좌표가 지도 내에 있고 / 0 <= nx < m : 방문할 x좌표가 지도 내에 있고
    # 방문할 좌표가 벽이 아니면 return

def append_to_Queue(ny, nx, k, time, visited, q) :
    if not visited[ny][nx][k] :             # 방문하지 않았다면
        visited[ny][nx][k] = True           # 방문 표시
        q.append((ny, nx, k, time + 1))     # time + 1 상태 q에 append

def solution(maps) :
    n, m = len(maps), len(maps[0])      # n : maps의 행 개수, m : maps의 열 개수
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]     # [False, False]를 m개의 열 개수만큼, n개의 행 개수만큼 생성
    # False for _ in range(2) : [False, False] 생성
    
    # dy, dx의 인덱스에 따라 상/하/좌/우 구별 가능 : dx[0] & dy[0] = 위로 이동
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    endY, endX = -1, -1     # 도착점의 x, y 좌표 넣는 변수. -1로 초기화한다
    q = deque()             # q라는 변수에 덱 기능 선언
    
    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == "S" :
                q.append((i, j, 0, 0))      # 덱 q에 시작점 좌표 입력 (q의 오른쪽 끝에 삽입)
                visited[i][j][0] = True     # (i, j) 좌표 방문 표시
            if maps[i][j] == "E" :
                endY, endX = i, j           # (i, j) 출구 좌표 입력
    
    while q :
        y, x, k, time = q.popleft()         # (q의 왼쪽 끝 원소 pop)
        # y좌표 , x좌표, 레버 동작 여부, 시작 지점부터 해당 좌표까지 가는 데 걸린 시간

        if y== endY and x == endX and k == 1 :      # 왜 k == 1이어야 할까..?
            return time
        
        for i in range(4) :     # 현재 좌표(y, x)에서 상하좌우 1칸씩 이동
            ny, nx = y + dy[i], x + dx[i]   # 이동한 좌표 ny, nx에 저장

            if not isValid(ny, nx, n, m, maps) :    
                continue                            # 이동 불가한 위치라면 continue
            
            if maps[ny][nx] == "L" :                            
                append_to_Queue(ny, nx, 1, time, visited, q)    # 이동한 곳이 레버라면 k = 1 적용
            else :
                append_to_Queue(ny, nx, k, time, visited, q)    # 이동한 곳이 레버가 아니라면 k = 0(그대로)

    return -1


    
#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))