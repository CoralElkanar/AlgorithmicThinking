"""
- Uses to find the shortest path in a weighted graph
- It is optimal
- It uses a greedy aproach
- Weights must be positive to guarantee correct results
- It finds the shortest path to every node from the origin

While any vertex remains unvisited:
    visit unvisited vertex with smallest known distance from the start vertex. Call this current_vertex.
    For each unvisited neighbor of current_vertex: 
        Calculate the new distance from the start vertex id this route is taken.
        If the calculated distance of this vertex is less than the known distance: 
            Update the distance for this neighbor.


Find the shortest distance from vertex A to vertex C

A --- 6 --- B
|        /  |  \  
|      /    |    5 
1    2      2      C
|   /       |     5
|  /        |  /
D --- 1 --- E 

"""

INF = float("infinity")

def dijkstra_algorithm(graph):
    min_distances = {vertex: INF for vertex in graph}
    unvisited_vertices = [vertex for vertex in graph]
    visited_vertices = []
    current_vertex = unvisited_vertices[0]  # the start node
    min_distances[current_vertex] = 0
    while unvisited_vertices:
        for neighbor in graph[current_vertex]:
            distance = graph[current_vertex][neighbor] + min_distances[current_vertex]
            if distance < min_distances[neighbor]:
                min_distances[neighbor] = distance
        visited_vertices.append(current_vertex)
        unvisited_vertices.remove(current_vertex)
        if unvisited_vertices:
            min_dist = min_distances[unvisited_vertices[0]]
            current_vertex = unvisited_vertices[0]
            for vertex in unvisited_vertices: 
                if min_distances[vertex] < min_dist:
                    current_vertex = vertex
    return min_distances



# define graph as dictionary representing adjacency list.
my_graph = {
    'U': {'V': 6, 'W': 7},
    'V': {'U': 6, 'X': 10},
    'W': {'U': 7, 'X': 1},
    'X': {'W': 1, 'V': 10},
}

print(my_graph)

minimum_distances = dijkstra_algorithm(graph=my_graph)
print(f"minimum_distances = {minimum_distances}")


my_graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1},

}

print(my_graph)

minimum_distances = dijkstra_algorithm(graph=my_graph)
print(f"minimum_distances = {minimum_distances}")
