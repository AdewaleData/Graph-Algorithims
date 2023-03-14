from collections import deque
#Breadth-First Search (BFS)
def bfs(graph, start):
    """
    Performs breadth-first search on the given graph starting from the given node.
    Returns a list of nodes in the order they were visited.
    """
    visited = {start}
    queue = deque([start])
    order = [start]

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                order.append(neighbor)

    return order
'''
The function takes a graph represented as a dictionary and a starting node as inputs,
and returns a list of nodes in the order they were visited using Breadth-First Search algorithm.
The algorithm visits all nodes at a given level before moving to the next level. It uses a queue data structure to keep track of the nodes to visit.


'''
#Depth-First Search (DFS)
def dfs(graph, start):
    """
    Performs depth-first search on the given graph starting from the given node.
    Returns a list of nodes in the order they were visited.
    """
    visited = set()
    order = []

    def dfs_recursive(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return order
    
    
'''
The function takes a graph represented as a dictionary and a starting node as inputs, 
and returns a list of nodes in the order they were visited using Depth-First Search algorithm. 
The algorithm explores as far as possible along each branch before backtracking. It uses a recursive function to implement the DFS algorithm.
'''


# Dijkstra's Algorithm:

import heapq

def dijkstra(graph, start):
    """
    Performs Dijkstra's algorithm on the given graph starting from the given node.
    Returns a dictionary of shortest paths to each node from the start node.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        (dist, node) = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances
'''
The function takes a weighted graph represented as a dictionary and a starting node as inputs, 
and returns a dictionary of shortest paths to each node from the start node using Dijkstra's algorithm. 
The algorithm works by maintaining a priority queue of nodes to visit and their current distances from the start node.
It repeatedly extracts the node with the smallest distance from the queue and updates the distances of its neighbors. 
It terminates when all nodes have been visited or the shortest path to the destination node has been found.

'''
