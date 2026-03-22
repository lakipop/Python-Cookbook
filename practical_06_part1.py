# %%
"""
Practical 06: Search Strategies and Propositional Logic
Part A – Uninformed Search Algorithms
"""

# %%
"""
1. Breadth-First Search (BFS) Traversal
"""
# Teaching Note: BFS explores the graph layer-by-layer. It uses a Queue (FIFO), which we build using `collections.deque` for performance.
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    print("BFS Traversal Order: ", end="")
    while queue:
        node = queue.popleft() # Pull from the front of the line
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # Push to the back of the line
    print() # newline

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A')

# %%
"""
Lab Task 01 - Problem 1: Modify BFS to return the shortest path between two nodes.
"""
# Teaching Note: To find the path, instead of just storing nodes in our queue, we store the *entire path* taken to reach that node. 
# Because BFS checks the shortest paths first, the first time we hit the target node, we are guaranteed it's the shortest path.
def bfs_shortest_path(graph, start, goal):
    visited = set()
    # Queue stores tuples of (current_node, [path_history])
    queue = deque([(start, [start])])
    visited.add(start)

    while queue:
        node, path = queue.popleft()
        
        if node == goal:
            return path
            
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None # If no path exists

print(f"Shortest path from A to E: {bfs_shortest_path(graph, 'A', 'E')}")

# %%
"""
Lab Task 01 - Problem 2: Apply BFS on a 2D grid maze.
"""
# Teaching Note: A 2D grid is just a graph where nodes are (x,y) coordinates and neighbors are up/down/left/right.
# 0 = Path, 1 = Wall.
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])]) # (coordinate, path_taken)
    visited = set()
    visited.add(start)

    # Directions: (row_move, col_move) -> Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == goal:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Ensure within grid bounds and not a wall (0 is path, 1 is wall)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
                    
    return None

start_pt, goal_pt = (0, 0), (4, 4)
maze_path = bfs_maze(maze, start_pt, goal_pt)
print(f"Maze Shortest Path: {maze_path}")

# %%
"""
2. Depth-First Search (DFS) Traversal
"""
# Teaching Note: DFS explores deeply down one path first using Recursion (which inherently uses the System Call Stack) 
# or an explicit iterative Stack (LIFO: list.pop()).
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
             dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start] # Standard Python list acts as a LIFO stack.
    
    while stack:
        node = stack.pop() # Pulls from the End/Top of the stack
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Reverse neighbors so left-most child is popped first (mimicking recursion order)
            stack.extend(reversed(graph[node]))

print("DFS Traversal (Recursive): ", end="")
dfs_recursive(graph, 'A')
print("\nDFS Traversal (Iterative): ", end="")
dfs_iterative(graph, 'A')
print()

# %%
"""
Lab Task 02 - Problem 1: Compare BFS and DFS traversal outputs
"""
# Teaching Note: Running them side-by-side proves how BFS maps across horizontal layers ('C' is hit before 'D'), 
# while DFS shoots straight down a branch until it is exhausted ('D' is hit before 'C').
advanced_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}
print("--- Comparison ---")
bfs(advanced_graph, 'A')
print("DFS Traversal Order: ", end="")
dfs_iterative(advanced_graph, 'A')
print()

# %%
"""
Lab Task 02 - Problem 2: Write a program to detect cycles using DFS.
"""
# Teaching Note: Cycle detection checks whether we run into a node that we are *currently visiting* in our active stack structure.
# We track 'visited' explicitly by keeping a separate active path memory 'rec_stack'.
def detect_cycle_dfs(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node) # Mark 'visiting in current path'

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if detect_cycle_dfs(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack: # Back-edge found! A cycle exists!
            return True

    rec_stack.remove(node) # Remove from active path traversing upward
    return False

# Graph WITH a cycle (A -> B -> C -> A)
cyclic_graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

v = set()
rs = set()
print("Cycle in cyclic_graph?", detect_cycle_dfs(cyclic_graph, 'A', v, rs))

# Graph WITHOUT a cycle (A -> B -> C)
acyclic_graph = {
    'A': ['B'],
    'B': ['C'],
    'C': []
}
v2 = set()
rs2 = set()
print("Cycle in acyclic_graph?", detect_cycle_dfs(acyclic_graph, 'A', v2, rs2))
