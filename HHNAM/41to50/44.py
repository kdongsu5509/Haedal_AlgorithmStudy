import heapq

def solution(N, road, K):
  graph = [[] for _ in range(N + 1)]
  distances = [float("inf")] * (N + 1)
  distances[1] = 0  

  for a, b, cost in road:
    graph[a].append((b, cost))
    graph[b].append((a, cost))

  heap = []
  heapq.heappush(heap, (0, 1))  
  while heap:
    dist, node = heapq.heappop(heap)

    for next_node, next_dist in graph[node]:
      cost = dist + next_dist
      if cost < distances[next_node]:
        distances[next_node] = cost
        heapq.heappush(heap, (cost, next_node))

  return sum(1 for dist in distances if dist <= K)