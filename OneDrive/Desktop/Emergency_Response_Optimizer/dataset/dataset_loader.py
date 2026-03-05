import osmnx as ox


def load_city_graph(city_name):

    print(f"Downloading road network for {city_name}...")

    graph = ox.graph_from_place(city_name, network_type="drive")

    print("Dataset loaded successfully")

    return graph