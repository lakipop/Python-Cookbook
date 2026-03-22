# %%
"""
Practical 06: Search Strategies and Propositional Logic
Part A – Uninformed Search Algorithms
"""

# %%
"""
1. Breadth-First Search (BFS) Traversal
"""
# --- TEACHING NOTE: BFS BASE ALGORITHM ---
# BFS explores the graph layer-by-layer. To do this, it relies on a Queue (First In, First Out). 
# The first node we see is the first node we process.
from collections import deque

def bfs(graph, start):
    visited = set()               # 1. Keep track of what we've seen so we don't loop endlessly.
    queue = deque([start])        # 2. Add our starting node to the line (queue).
    visited.add(start)            # 3. Immediately mark the start node as 'seen'.
    
    print("BFS Traversal Order: ", end="")
    while queue:                  # 4. As long as there are people in line...
        node = queue.popleft()    # 5. Take the first person out of the front of the line.
        print(node, end=" ")
        
        # 6. Check all the neighbors of the node we just popped.
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)      # 7. Mark neighbor as seen.
                queue.append(neighbor)     # 8. Put them at the BACK of the line.
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
# --- TEACHING NOTE: BFS SHORTEST PATH ---
# Normally, BFS just spits out every node it sees. To find the actual Shortest Path, 
# instead of just putting a single `node` into the queue, we put a Tuple containing (current_node, history_of_path_taken).
# Because BFS searches layer 1, then layer 2 equally in all directions... the very first time 
# you bump into the `goal` node, you are mathematically guaranteed to have taken the shortest route!
def bfs_shortest_path(graph, start, goal):
    visited = set()
    # Queue stores tuples of (current_node, [path_history]) e.g. ('A', ['A'])
    queue = deque([(start, [start])])
    visited.add(start)

    while queue:
        node, path = queue.popleft() # Unpack the tuple
        
        # If we found the target, immediately return the path we took to get here!
        if node == goal:
            return path
            
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # We add the neighbor to the back of the line, AND we give them 
                # a copy of the path that took us here, plus themselves!
                queue.append((neighbor, path + [neighbor]))
                
    return None # If no path exists

print(f"Shortest path from A to E: {bfs_shortest_path(graph, 'A', 'E')}")

# %%
"""
Lab Task 01 - Problem 2: Apply BFS on a 2D grid maze.
"""
# --- TEACHING NOTE: 2D GRID MAZE ---
# A maze is just a graph. Instead of letter names like 'A', the nodes are coordinates (row, column).
# Instead of checking a dictionary for neighbors, you check adjacent blocks: Up, Down, Left, Right.
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    # Start queue holding the coordinate and the path history: ((0,0), [(0,0)])
    queue = deque([(start, [start])]) 
    visited = set()
    visited.add(start)

    # These are mathematical vectors to move [Right, Down, Left, Up] on a 2D grid
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (r, c), path = queue.popleft() # Current Row & Column, and the Path History

        if (r, c) == goal:
            return path

        # For every direction (Up, Down, Left, Right)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Ensure within grid bounds and not walls (0 is path, 1 is wall)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # Add this valid new coordinate to the line, alongside the path updating!
                    queue.append(((nr, nc), path + [(nr, nc)]))
                    
    return None

start_pt, goal_pt = (0, 0), (4, 4)
maze_path = bfs_maze(maze, start_pt, goal_pt)
print(f"Maze Shortest Path: {maze_path}")

# %%
"""
2. Depth-First Search (DFS) Traversal
"""
# --- TEACHING NOTE: DFS BASE ALGORITHM ---
# DFS goes as deep as possible into one branch before checking others. 
# It relies on a Stack (Last In, First Out). Think of a stack of plates—you always pull off the top plate.
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)          # 1. Mark current node as seen.
    print(start, end=" ")
    
    # 2. Look at neighbors.
    for neighbor in graph[start]:
        if neighbor not in visited:
             # 3. Immediately dive deep! We pause this function and start a new one on the neighbor.
             dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start] # 1. Lists natively act as a Stack using .append() and .pop()
    
    while stack:
        node = stack.pop() # 2. Pull from the TOP of the stack (the most recent item)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            # 3. Add neighbors to the TOP of the stack. We reverse them so the 
            # left-most child sits on the absolute top of the stack and gets processed first.
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
# --- TEACHING NOTE: DFS vs BFS ---
# BFS prints layers: A spreads out and touches B and C (Layer 1) before touching any of their children.
# DFS acts like tracing a limb on a tree. It hits A, goes to B, and immediately drills down to B's children 
# (D, E) until a dead end is hit, completely ignoring C until the very end.
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
print("--- BFS vs DFS Output Comparison ---")
bfs(advanced_graph, 'A')
print("DFS Traversal Order: ", end="")
dfs_iterative(advanced_graph, 'A')
print()

# %%
"""
Lab Task 02 - Problem 2: Write a program to detect cycles using DFS.
"""
# --- TEACHING NOTE: CYCLE DETECTION ---
# 'visited' stores EVERY node we ever hit. 
# 'rec_stack' ONLY stores the nodes we are physically standing on *right now* in our active branch.
def detect_cycle_dfs(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node) # 1. Mark this node as "Currently Active in our Path"

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            # Dive deeper
            if detect_cycle_dfs(graph, neighbor, visited, rec_stack):
                return True
        # 2. THE SECRET: If the neighbor is already in our *active path memory*, we walked in a circle!
        elif neighbor in rec_stack: 
            return True

    # 3. We hit a dead end and are backtracking upward. 
    # Take this node off the active path memory, since we are leaving it.
    rec_stack.remove(node) 
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
