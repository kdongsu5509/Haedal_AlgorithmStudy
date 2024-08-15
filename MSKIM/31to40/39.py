from collections import deque

def solution(graph, start):
    adj_list = {}  #
    for u, v in graph:
        if u in adj_list:
            adj_list[u].append(v)
        else:
            adj_list[u] = [v]


    def bfs(start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = [start]

        while queue:
            node = queue.popleft()
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        result.append(neighbor)

        return result

    return bfs(start)


graph = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
start_node = 'A'

print(solution(graph, start_node))
