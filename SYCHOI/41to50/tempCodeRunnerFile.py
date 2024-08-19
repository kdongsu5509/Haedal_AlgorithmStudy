    if is_blocked(new_x, new_y) :
                continue

            new_cost = calculate_cost(direction, prev_direction, cost)

            if (new_x, new_y) == (N - 1, N - 1) :
                answer = min(answer, new_cost)
            elif isShouldUpdate(new_x, new_y, direction, new_cost) :
                queue.append((new_x, new_y, direction, new_cost))
                visited[new_x][new_y][direction] = new_cost