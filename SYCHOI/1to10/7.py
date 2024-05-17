def solution(dirs) :
    xPath = [[0 for _ in range(11)] for _ in range(11)]
    yPath = [[0 for _ in range(11)] for _ in range(11)]
    x, y = 5, 5; cnt = 0

    for D in str(dirs) :    # 왜 dirs만 하면 D 출력이 안될까..
        if D == "U" :
            if y != 0 :                 # 이동하려는 위치가 좌표평면 안이라면 
                y -= 1                  # 이동
                if yPath[y+1][y] != 1 :     # 처음 걸어본 길이라면
                    yPath[y+1][y] = 1       # y -> y-1 흔적 (1)
                    cnt += 1                
        elif D == "D" :
            if y != 10 :                # 이동하려는 위치가 좌표평면 안이라면 
                y += 1                  # 이동
                if yPath[y-1][y] != 1 :     # 처음 걸어본 길이라면
                    yPath[y-1][y] = 1       # y -> y+1 흔적 (1)
                    cnt += 1                
        elif D == "L" :
            if x != 0 :                 # 이동하려는 위치가 좌표평면 안이라면
                x -= 1                  # 이동
                if xPath[x+1][x] != 1 :     # 처음 걸어본 길이라면
                    xPath[x+1][x] = 1       # x -> x-1 흔적 (1)
                    cnt += 1
        elif D == "R" :
            if x != 10 :                # 이동하려는 위치가 좌표평면 안이라면
                x += 1                  # 이동
                if xPath[x-1][x] != 1 :     # 처음 걸어본 길이라면
                    xPath[x-1][x] = 1       # x -> x+1 흔적 (1)
                    cnt += 1
    
    return cnt
    



#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution('ULURRDLLU'))
# print(solution('LULLLLLLU'))
# print(solution('LURRDLLURRDLLURRDLLURRDL'))
# print(solution('UUUUUUUUUUURRRRRRRRRR'))
# print(solution('LLLLLLLLLLDDDDDDDDD'))