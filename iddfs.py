def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nSearching at depth: {depth}")
        visited = set()
        if dls(graph, start, goal, depth, visited):
            return True
    return False


def dls(graph, node, goal, depth, visited):
    if depth < 0:
        return False

    print(f"Visiting: {node}")

    if node == goal:
        print("Goal found!")
        return True

    if depth == 0:
        return False

    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth - 1, visited):
                return True

    return False




graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))



found = iddfs(graph, start_node, goal_node, max_depth)

if not found:
    print("Goal not found within depth limit.")