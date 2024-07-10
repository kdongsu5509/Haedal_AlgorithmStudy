from collections import deque

def is_valid_move(ny,nx,m,maps):
    return 0<=ny<nx and 0<=nx<m and maps[ny][nx]!="X"

def append_to_queue(ny,nx,k,time,visited,q):
    if not visited[ny][nx][k]:
        visited[ny][nx][k]=True
        q.append((ny,nx,k,time+1))

def solution(maps):
    n,m=len(maps),len(maps[0])
    visited=[[[False for _ in range(2)] for _ in range(m) for _ in range(n)]]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque()
    end_y,end_x=-1,-1

    for i in range(n):
        for j in range(m):
            if maps[i][j]=="S":
                q.append((i,j,0,0))
                visited[i][j][0]=True
            if maps[i][j]=="E":
                end_y,end_x=i,j

    while q:
        y,x,k,time=q.popleft()

        if y==end_y and x==end_x and k==1:
            return time

        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if not is_valid_move(ny,nx,m,maps):
                continue

            if maps[ny][nx]=="L":
                append_to_queue(ny,nx,1,time,visited,q)
            else:
                append_to_queue(ny,nx,k,time,visited,q)
        return -1