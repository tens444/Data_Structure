import Queue

graph = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}

def BFS(graph, start):
    queue = []
    queue.append(start)
    visited = set()
    while queue:
        cur = queue.pop(0)
        visited.add(cur)
        for n in graph[cur]:
            if n not in queue and n not in visited:
                queue.append(n)

def DFS(graph, start):
    stack = []
    stack.append(start)
    visited = set()
    while stack:
        cur = stack.pop()
        visited.add(cur)
        for n in graph[cur]:
            if n not in stack and n not in visited:
                stack.append(n)