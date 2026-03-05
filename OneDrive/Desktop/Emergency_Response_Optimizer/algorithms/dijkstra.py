import heapq


def dijkstra(graph, start):

    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, edge_data in graph[current_node].items():

            weight = edge_data[0].get("length", 1)

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances