# Emergency Response System Optimizer 

An Advanced Data Structures and Algorithms project that optimizes emergency response using graph algorithms and real-world road network data.

## Overview

This project simulates an emergency dispatch system that determines the fastest route for emergency vehicles (ambulances, fire trucks, etc.) to reach an incident location.

The system models a city as a graph where:

* Nodes represent intersections
* Edges represent roads
* Edge weights represent travel distance or time

Using graph algorithms, the system identifies the optimal dispatch route and visualizes the response on an interactive map.

## Features

* Large-scale road network dataset
* Shortest path algorithms (Dijkstra / A*)
* Emergency vehicle dispatch optimization
* Animated route visualization
* Interactive dashboard

## Tech Stack

Python
NetworkX
OSMnx
Streamlit
Folium

## Project Structure

```
emergency-response-optimizer
│
├── algorithms
├── dataset
├── simulation
├── visualization
├── frontend
├── utils
├── tests
├── data
│
├── main.py
├── requirements.txt
└── README.md
```

## Run the Project

Install dependencies:

pip install -r requirements.txt

Run the frontend:

streamlit run frontend/app.py
