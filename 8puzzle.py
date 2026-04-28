import heapq

# Goal State
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Possible Moves
MOVES = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1)
}


class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth  # g(n)
        self.blank_pos = self.find_blank()

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)

    def is_goal(self):
        return self.state == GOAL_STATE

    def display(self):
        for row in self.state:
            print(row)
        print()

    def get_successors(self):
        successors = []
        x, y = self.blank_pos

        for move, (dx, dy) in MOVES.items():
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state]

                # Swap blank with neighbor
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]

                successors.append(Puzzle(new_state, self, move, self.depth + 1))

        return successors

    # Manhattan Distance Heuristic
    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                val = self.state[i][j]
                if val != 0:
                    goal_x = (val - 1) // 3
                    goal_y = (val - 1) % 3
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def __lt__(self, other):
        return False  # needed for heapq


# A* Algorithm
def a_star(initial_state):
    start = Puzzle(initial_state)

    open_list = []
    heapq.heappush(open_list, (start.depth + start.manhattan(), start))

    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current.is_goal():
            return current

        visited.add(tuple(map(tuple, current.state)))

        for neighbor in current.get_successors():
            state_tuple = tuple(map(tuple, neighbor.state))

            if state_tuple not in visited:
                f_cost = neighbor.depth + neighbor.manhattan()
                heapq.heappush(open_list, (f_cost, neighbor))

    return None


# Print solution
def print_solution(goal_node):
    path = []
    while goal_node:
        path.append(goal_node)
        goal_node = goal_node.parent

    path.reverse()

    print("Solution Steps:\n")
    for i, step in enumerate(path):
        print(f"Move {i}: {step.move if step.move else 'Start'}")
        step.display()


# Example Initial State
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Run A*
solution = a_star(initial_state)

if solution:
    print("Solution Found!\n")
    print_solution(solution)
else:
    print("No solution found.")