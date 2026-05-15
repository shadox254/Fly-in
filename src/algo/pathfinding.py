# *************************************************************************** #
#                                                                             #
#     |\      _,,,---,,_                                                      #
#     /,`.-'`'    -.  ;-;;,_                                                  #
#    |,4-  ) )-,_. ,\ (  `'-'                                                 #
#   '---''(_/--'  `-'\_)         __..--''``---....___   _..._    __           #
#                            _.-'    .-/";  `        ``<._  ``.''_ `.         #
#                        _.-' _..--.'_    \                    `( ) )         #
#                       (_..-' // (< _     ;_..__               ; `'          #
#                                  `-._,_)' // / ``--...____..-'              #
#                                                                             #
# *************************************************************************** #
#  File: pathfinding.py                                                       #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/05/13 09:35:23 by rruiz                                      #
#  Updated: 2026/05/15 08:48:16 by rruiz                                      #
# *************************************************************************** #

import heapq

def calculate_drone_path(start_hub_name, end_hub_name, start_turn, calendar, hubs, connections):
    queue = []
    heapq.heappush(queue, (0, start_turn, start_hub_name, [(start_turn, start_hub_name)]))
    visited = set()

    while queue:
        cost, current_turn, current_hub, path = heapq.heappop(queue)
        state = (current_turn, current_hub)

        if state in visited:
            continue
        visited.add(state)

        if current_hub == end_hub_name:
            return path

        max_d = hubs[current_hub].max_drones
        if calendar.is_hub_available(current_hub, current_turn + 1, max_d):
            heapq.heappush(queue, (cost + 1, current_turn + 1, current_hub, path + [(current_turn + 1, current_hub)]))

        if current_hub in connections:
            for neighbor, cap in connections[current_hub].items():
                n_type = hubs[neighbor].zone_type
                
                if n_type == 'blocked':
                    continue
                    
                if n_type == 'restricted':
                    move_cost = 2
                else:
                    move_cost = 1
                arrival_turn = current_turn + move_cost

                conn_available = True
                for t in range(current_turn + 1, arrival_turn + 1):
                    if not calendar.is_connection_available(current_hub, neighbor, t, cap):
                        conn_available = False
                        break
                
                if not conn_available:
                    continue

                n_max_d = hubs[neighbor].max_drones
                if calendar.is_hub_available(neighbor, arrival_turn, n_max_d):
                    heapq.heappush(queue, (cost + move_cost, arrival_turn, neighbor, path + [(arrival_turn, neighbor)]))

    return None