# Sakhal Dijkstra’s Pathfinder
Shortest-path finder for DayZ Sakhal using Dijkstra’s algorithm.

## Overview
- **Features**: Weighted paths (main=1x, dirt=1.5x), interactive input, error handling.
- **Nodes**: 6 towns (Aniva, Nogovo, Petropavlovsk, Rudnogorsk, Severonorsk, Burukan) + Geothermal Energy Station.
- **Tools**: Python, heapq, adjacency list, iZurvive data, Paint for visualization.
- **Run**: `python sakhal_dijkstra.py`, enter a node (e.g., "GeoES").

## Shortest Paths
- Aniva → Severonorsk: 12.77 units ([map](maps/shortest_aniva_to_severonorsk.png))
- Aniva → Nogovo: 8.13 units ([map](maps/shortest_aniva_to_nogovo.png))
- Nogovo → Burukan: 11.12 units ([map](maps/shortest_nogovo_to_burukan.png))
- Nogovo → Rudnogorsk: 15.32 units ([map](maps/shortest_nogovo_to_rudnogorsk.png))
- Nogovo → Severonorsk: 12.91 units ([map](maps/shortest_nogovo_to_severonorsk.png))
- Petro → Severonorsk: 7.60 units ([map](maps/shortest_petro_to_severonorsk.png))
- Petro → Nogovo: 6.45 units ([map](maps/shortest_petro_to_nogovo.png))
- Petro → Burukan: 8.54 units ([map](maps/shortest_petro_to_burukan.png))
- Rudnogorsk → Severonorsk: 4.68 units ([map](maps/shortest_rudnogorsk_to_severonorsk.png))
- Nogovo → GeoES: 3.89 units ([map](maps/shortest_nogovo_to_geoes.png))
- Petro → GeoES: 3.64 units ([map](maps/shortest_petro_to_geoes.png))
- Severonorsk → GeoES: 9.92 units ([map](maps/shortest_severonorsk_to_geoes.png))
