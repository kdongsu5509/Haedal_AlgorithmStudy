from collections import deque
direction = [[1,0], [-1,0], [0,1], [0,-1]]

def solution(maps):
    answer = 0
    X = len(maps)
    Y = len(maps[0])
    for i in range(X):
        for j in range(Y):
            if maps[i][j] == 'S':
                sx, sy = i, j
    
    lever = False
    visited = [[False] * Y for _ in range(X)]
    visited_l = [a[:] for a in visited]
    q = deque([[sx, sy, 0, lever]])
    
    while q:
        x, y, deph, lever = q.popleft()
        
        if not lever:
            visited[x][y] = True
        else:
            visited_l[x][y] = True
        
        if maps[x][y] == 'L':
            lever = True
            visited_l[x][y] = True
            
        if lever and maps[x][y] == 'E' and visited_l[x][y]:
            return deph
            
        for d in direction:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < X and 0 <= ny < Y:
                if not lever:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append([nx,ny,deph+1, lever])
                else:
                    if not visited_l[nx][ny] and maps[nx][ny] != 'X':
                        visited_l[nx][ny] = True
                        q.append([nx,ny,deph+1, lever])
                    
    return -1