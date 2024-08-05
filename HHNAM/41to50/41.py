def solution(graph, source):
  num_vertices = len(graph)

  distance = [float("inf")] * num_vertices
  distance[source] = 0

  predecessor = [None] * num_vertices

  for temp in range(num_vertices - 1):
    for u in range(num_vertices):
      for v, weight in graph[u]:
        if distance[u] + weight < distance[v]:
          distance[v] = distance[u] + weight
          predecessor[v] = u

  for u in range(num_vertices):
    for v, weight in graph[u]:
      if distance[u] + weight < distance[v]:
        return [-1]
  return [distance, predecessor]

print(solution([[(1, 4), (2, 3), (4, -6 )], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)],[(2, 2)]],0))
print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]],0))