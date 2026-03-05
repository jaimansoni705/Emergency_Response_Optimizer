import folium


def visualize_route(graph, path):

    start_node = graph.nodes[path[0]]

    m = folium.Map(
        location=[start_node["y"], start_node["x"]],
        zoom_start=13
    )

    coordinates = []

    for node in path:
        lat = graph.nodes[node]["y"]
        lon = graph.nodes[node]["x"]
        coordinates.append((lat, lon))

    folium.PolyLine(
        coordinates,
        color="red",
        weight=5
    ).add_to(m)

    return m