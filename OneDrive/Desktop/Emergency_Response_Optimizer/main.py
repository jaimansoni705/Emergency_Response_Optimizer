"""
Main entry point for the Emergency Response System Optimizer
"""

from dataset.dataset_loader import load_city_graph
from algorithms.dispatcher import dispatch_vehicle


def main():

    print("Emergency Response System Optimizer")

    # Load road network dataset
    city = "Mumbai, India"
    graph = load_city_graph(city)

    print("Road network loaded")

    # Example station and incident nodes
    stations = [list(graph.nodes)[0]]
    incident = list(graph.nodes)[100]

    station, path, distance = dispatch_vehicle(graph, stations, incident)

    print("Dispatching vehicle...")
    print("Station:", station)
    print("Distance:", distance)


if __name__ == "__main__":
    main()