from queue import PriorityQueue, Queue


# BFS algorithm
def bfs(graph, start, goal):
    queue = Queue()
    queue.put([start])
    visited = set()

    while not queue.empty():
        path = queue.get()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for (neighbor, _) in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.put(new_path)

    return None

# DFS algorithm
def dfs(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    visited.add(start)

    if start == goal:
        return path

    for (neighbor, _) in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result

    return None

# UCS algorithm
def ucs(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, [start]))  # (cost, path)

    while not pq.empty():
        (cost, path) = pq.get()
        node = path[-1]

        if node == goal:
            return path

        for (neighbor, weight) in graph.get(node, []):
            new_cost = cost + weight
            new_path = path + [neighbor]
            pq.put((new_cost, new_path))

    return None

# Greedy Best-First Search
def greedy_bfs(graph, start, goal, heuristics):
    pq = PriorityQueue()
    pq.put((heuristics[start], [start]))

    while not pq.empty():
        (heuristic_value, path) = pq.get()
        node = path[-1]

        if node == goal:
            return path

        for (neighbor, _) in graph.get(node, []):
            new_path = path + [neighbor]
            pq.put((heuristics[neighbor], new_path))

    return None

# A* algorithm
def a_star(graph, start, goal, heuristics):
    pq = PriorityQueue()
    pq.put((0 + heuristics[start], 0, [start]))

    while not pq.empty():
        (estimated_cost, cost, path) = pq.get()
        node = path[-1]

        if node == goal:
            return path

        for (neighbor, weight) in graph.get(node, []):
            new_cost = cost + weight
            new_path = path + [neighbor]
            estimated_cost = new_cost + heuristics[neighbor]
            pq.put((estimated_cost, new_cost, new_path))

    return None
