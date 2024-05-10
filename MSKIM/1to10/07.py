def is_valid_move(nx,ny):
    return 0<=nx<11 and 0<=ny<11

def update_location(x,y,dir):
    if dir=='U':
        nx,ny=x,y+1
    elif dir=='D':
        nx,ny=x,y-1
    elif dir=='L':
        nx,ny=x-1,y
    elif dir=='R':
        nx,ny=x+1,y
    return nx,ny

def solution(dirs):
    #음수없애려고 5,5로 시작
    x,y=5,5
    #겹치는 좌표는 하나로 처리
    tmp=set()
    for dir in dirs:
        nx,ny=update_location(x,y,dir)
        if not is_valid_move():
            continue
        # M.P)!! 양방향으로 추가해줘야함
        tmp.add((x,y,nx,ny))
        tmp.add((nx,ny,x,y))
        x,y=nx,ny
    return len(tmp)/2