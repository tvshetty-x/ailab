def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    print(f"Visiting: {start}")

    visited.add(start)
    path.append(start)

    if start == goal:
        print("Goal found!")
        print("Path:", " -> ".join(path))
        return True

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited, path):
                return True

    path.pop()  # backtrack
    return False


graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

found = dfs(graph, start_node, goal_node)

if not found:
    print("Goal not found.")