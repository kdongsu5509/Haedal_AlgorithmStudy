def solution(board, moves):
    pang_cnt = 0
    board_row = len(board)
    board_col = len(board[0])
    basket = [0]
    print(board_row, board_col)
    
    for pick_col in moves:
        for row in range(board_row):
            if(board[row][pick_col-1] != 0):
                if(basket[-1] == board[row][pick_col-1]):
                    basket.pop()
                    pang_cnt += 2
                    board[row][pick_col-1] = 0
                    break
                else:
                    basket.append(board[row][pick_col-1])
                    board[row][pick_col-1] = 0
                    break
                
    return pang_cnt