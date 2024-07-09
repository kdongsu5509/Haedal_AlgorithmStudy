def solution(board, moves) :
    cnt = 0
    bsk = []
    
    for i in moves :                        # i는 열(실제 열 인덱스는 i-1)
        for j in range(len(board[0])) :     # j는 행

            if board[j][i-1] != 0 :                     # i열에 인형이 있다면 뽑기
                bsk.append(board[j][i-1])               # 뽑아서 바구니에 넣기
                board[j][i-1] = 0                       # 뽑으면 위치의 숫자 0이 됨

                if len(bsk) > 1 and bsk[-1] == bsk[-2] :    # 바구니에 인형이 2개 있고 바구니 top에 있는 것(-2)과 지금 뽑은 것(-1)이 같으면
                    cnt += 2                                # 뽑은 개수 업데이트
                    bsk.pop(); bsk.pop()                    # 바구니에 있는 인형 두 개 없애기
                
                break

    return cnt



#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))