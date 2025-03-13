import heapq
# Tommy Feeley March 2025
graph = {
    "Aniva": [("Severonorsk", 12.77), ("Nogovo", 8.13)],
    "Nogovo": [("Aniva", 8.13), ("Burukan", 11.12), ("Rudnogorsk", 15.32), ("Severonorsk", 12.91), ("Petro", 6.45), ("GeoES", 3.89)],
    "Burukan": [("Nogovo", 11.12), ("Petro", 8.54)],
    "Rudnogorsk": [("Nogovo", 15.32), ("Severonorsk", 4.68)],
    "Severonorsk": [("Aniva", 12.77), ("Nogovo", 12.91), ("Petro", 7.60), ("Rudnogorsk", 4.68), ("GeoES", 9.92)],
    "Petro": [("Severonorsk", 7.60), ("Nogovo", 6.45), ("Burukan", 8.54), ("GeoES", 3.64)],
    "GeoES": [("Nogovo", 3.89), ("Petro", 3.64), ("Severonorsk", 9.92)]
}

# Dijsktra's Algorithm using our graph (adjacency list), distances (dictionary), priority_queue (minimum heap)

def dijkstra(graph, start):
    # Dictionary thats storing our results (distance between nodes), we're appending to it on 3rd to last line of algorithm
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # priority queue is a Heap using heapq. Minimum heap specifically, to keep track of the shortest distance between nodes (Cities)
    priority_queue = [(0, start)]
    while priority_queue:
        # heapqpop(priority_queue) is popping top of our heap, when you pop it returns the closest node and we can assign returned value
        # It would be O(n) to go through list of all nodes but using heap + heappop/heappush, we are O(log n) time, a lot better
        # Doesn't really matter much while we have so few nodes. Would be significant if Sakhal fully mapped
        curr_dist, curr = heapq.heappop(priority_queue)
        if curr_dist > distances[curr]:
            continue
        for neighbor, weight in graph[curr]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# Get starting node (starting city in normal terms) from user, running dijkstras from start node to other mapped nodes
while True:
    start = input("Enter start node (Aniva, Nogovo, Burukan, Rudnogorsk, Severonorsk, Petropavlovsk, GeoES): ").strip()
    if start in graph:
        result = dijkstra(graph, start)
        print(f"\nShortest paths from {start}:")
        for node, dist in result.items():
            print(f"{node}: {dist:.2f} units")
        break  # Exit loop if valid
    else:
        print("Error: Invalid node! You may have entered a unmapped starting city, or made a typo!")
