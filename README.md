# Sakhal Dijkstra’s Pathfinder
Shortest-path finder for DayZ Sakhal using Dijkstra’s algorithm.
7 node, 12 edge Sakhal graph representing distance between Sakhal loot spots

## Overview
- **Features**: Weighted paths (main=1x, dirt=1.5x), interactive input, error handling.
- **Nodes**: 6 towns (Aniva, Nogovo, Petropavlovsk, Rudnogorsk, Severonorsk, Burukan) + Geothermal Energy Station.
- **Tools**: Python, heapq, adjacency list, min heap, iZurvive data, Paint for visualization.
- **Complexity**:
  - **Time**: O((n + e) log n) — Min-heap (heapq) optimizes node selection.
  - **Space**: O(n + e) — Stores graph (adjacency list), distances, and heap.
  - (n = 7 nodes, e = 12 edges)
- **Run**: `python sakhal_dijkstra.py`, enter a node (e.g., "GeoES").

## Shortest Paths (1 unit = 1 km)
- Aniva → Severonorsk: 12.77 units ([map](/maps_final/map_route_aniva_severomorsk.png))
- Aniva → Nogovo: 8.13 units ([map](maps_final/map_route_nogovo_aniva.png))
- Nogovo → Burukan: 11.12 units ([map](maps_final/map_route_nogovo_burukan.png))
- Nogovo → Rudnogorsk: 15.32 units ([map](maps_final/map_route_nogovo_rudnogorsk.png))
- Nogovo → Severonorsk: 12.91 units ([map](maps_final/map_route_nogovo_severonorsk.png))
- Petro → Severonorsk: 7.60 units ([map](maps_final/map_route_petro_severomorsk.png))
- Petro → Nogovo: 6.45 units ([map](maps_final/map_route_petro_nogovo.png))
- Petro → Burukan: 8.54 units ([map](maps_final/map_route_petro_burukan.png))
- Rudnogorsk → Severonorsk: 4.68 units ([map](maps_final/map_route_rudnogorsk_severonorsk.png))
- Nogovo → GeoES: 3.89 units ([map](maps_final/map_route_nogovo_geoES.png))
- Petro → GeoES: 3.64 units ([map](maps_final/map_route_petro_geoES.png))
- Severonorsk → GeoES: 9.92 units ([map](maps_final/map_route_severonorsk_geoES.png))
