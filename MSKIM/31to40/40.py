import heapq

def solution(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = []

    heapq.heappush(queue, [distances[start], start])
    paths = {start: [start]}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                paths[adjacent_node] = paths[current_node] + [adjacent_node]

                heapq.heappush(queue, [distance, adjacent_node])

    sorted_paths = {node: paths[node] for node in sorted(paths)}
    return [distances, sorted_paths]


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'

print(solution(graph, start_node))
