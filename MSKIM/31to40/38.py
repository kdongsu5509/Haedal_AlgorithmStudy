#난 dic쓸거임

def solution(graph, start):
    adj_list = {}

    for u, v in graph:
        if u in adj_list:
            adj_list[u].append(v)
        else:
            adj_list[u] = [v]


    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)

        if node in adj_list:
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, result)

    visited = set()
    result = []
    dfs(start, visited, result)
    return result

graph = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
start_node = 'A'

print(solution(graph, start_node))
