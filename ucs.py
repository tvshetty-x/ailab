class PriorityQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0]) 
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    def is_empty(self):
        return len(self.queue) == 0
def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.enqueue((start, [start]), 0)
    visited = {}
    while not pq.is_empty():
        cost, (node, path) = pq.dequeue()
        if node == goal:
            return cost, path
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        for neighbor, weight in graph[node]:
            pq.enqueue((neighbor, path + [neighbor]), cost + weight)
    return float("inf"), []
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    edges = int(input(f"Enter number of neighbors for {node}: "))
    graph[node] = []
    for _ in range(edges):
        neighbor = input("Enter neighbor: ")
        cost = int(input("Enter cost: "))
        graph[node].append((neighbor, cost))
start = input("Enter start node: ")
goal = input("Enter goal node: ")
cost, path = uniform_cost_search(graph, start, goal)

print("Cost and Path:", (cost, path))