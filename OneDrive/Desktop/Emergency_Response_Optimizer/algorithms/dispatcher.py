import networkx as nx


def dispatch_vehicle(graph, stations, incident):

    best_station = None
    best_distance = float("inf")
    best_path = None

    for station in stations:

        try:
            path = nx.shortest_path(graph, station, incident, weight="length")
            distance = nx.shortest_path_length(graph, station, incident, weight="length")

            if distance < best_distance:
                best_station = station
                best_distance = distance
                best_path = path

        except:
            continue

    return best_station, best_path, best_distance