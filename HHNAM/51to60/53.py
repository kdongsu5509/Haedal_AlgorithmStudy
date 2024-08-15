def solution(board, aloc, bloc):
  ROW, COL = len(board), len(board[0])
  DR, DC = [-1, 0, 1, 0], [0, 1, 0, -1]

  def is_valid_pos(r, c):
    return 0 <= r < ROW and 0 <= c < COL

  def recursive_func(alpha_pos, beta_pos, visited, step):
    r, c = alpha_pos if step % 2 == 0 else beta_pos
    can_move = False
    is_opponent_winner = True
    win_steps, lose_steps = [], []

    for i in range(4):
      nr, nc = r + DR[i], c + DC[i]
      if is_valid_pos(nr, nc) and (nr, nc) not in visited and board[nr][nc]:
        can_move = True
        if alpha_pos == beta_pos:
          return True, step + 1

        win, steps_left = (
          recursive_func([nr, nc], beta_pos, visited | {(r, c)}, step + 1)
          if step % 2 == 0
          else recursive_func(
            alpha_pos, [nr, nc], visited | {(r, c)}, step + 1
          )
        )
        is_opponent_winner &= win
        (win_steps if win else lose_steps).append(steps_left)

    if not can_move:
      return False, step
    if is_opponent_winner:
      return False, max(win_steps)
    return True, min(lose_steps)

  _, steps = recursive_func(aloc, bloc, set(), 0)
  return steps