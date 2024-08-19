def solution(keyinput, board):
  x, y = 0, 0
  moves = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
  width, height = board[0] // 2, board[1] // 2

  def is_in_bounds(x, y, dx, dy):
    return -width <= x + dx <= width and -height <= y + dy <= height

  for key in keyinput:
    dx, dy = moves[key]
    if is_in_bounds(x, y, dx, dy):
      x += dx
      y += dy

  return [x, y]