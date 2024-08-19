f dfs(node, visited, result) :
        visited.add(node)
        result.append(node)
        for neighbor in adj_list.get(node, []) :
            if neighbor not in visited :
                dfs(neighbor, visited, result)

        visited = set()
        result = []
        dfs(start, visited, result)
        return result