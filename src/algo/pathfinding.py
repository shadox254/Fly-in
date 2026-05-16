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
#  Updated: 2026/05/16 10:55:59 by rruiz                                      #
# *************************************************************************** #

import heapq
from src.models.calendar import ReservationCalendar
from src.models.hub import Hub
from src.models.errors import MapFileError


def calculate_drone_path(
        start_hub_name: str,
        end_hub_name: str,
        start_turn: int,
        calendar: ReservationCalendar,
        hubs: dict[str, Hub],
        connections: dict[str, dict[str, int]]
        ) -> list[tuple[int, str]] | None:
    '''Find the shortest valid path for a drone using a time-expanded Dijkstra
    algorithm.

    This function accounts for hub capacities, connection limits, and
    zone-based movement costs. It explores states defined by both location and
    time (turn) to avoid collisions and respect network constraints.

    Args:
        start_hub_name (str): The name of the departure hub.
        end_hub_name (str): The name of the destination hub.
        start_turn (int): The turn at which the drone begins its journey.
        calendar (ReservationCalendar): The global registry of resource
            occupancy.
        hubs (dict[str, Hub]): Dictionary containing all hub data and
            capacities.
        connections (dict[str, dict[str, int]]): Nested adjacency map with
            link capacities.

    Returns:
        list[tuple[int, str]] | None: A list of (turn, hub_name) representing
            the scheduled path if successful, or None if no path is available.
    '''
    queue: list[tuple[int, int, int, str, list[tuple[int, str]]]] = []
    heapq.heappush(queue, (0, 0, start_turn, start_hub_name,
                           [(start_turn, start_hub_name)]))
    visited = set()

    while queue:
        cost, prio, current_turn, current_hub, path = heapq.heappop(queue)
        state = (current_turn, current_hub)

        if current_turn > 1000:
            raise MapFileError('Error, no path was found on this map '
                               '(>1000 turn)')

        if state in visited:
            continue
        visited.add(state)

        if current_hub == end_hub_name:
            return path

        max_d = hubs[current_hub].max_drones
        if calendar.is_hub_available(current_hub, current_turn + 1, max_d):
            heapq.heappush(queue,
                           (cost + 1, prio, current_turn + 1, current_hub,
                            path + [(current_turn + 1, current_hub)]))

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

                if n_type == 'priority':
                    new_prio = prio - 1
                else:
                    new_prio = prio

                conn_available = True
                for t in range(current_turn + 1, arrival_turn + 1):
                    if not calendar.is_connection_available(current_hub,
                                                            neighbor, t, cap):
                        conn_available = False
                        break

                if not conn_available:
                    continue

                n_max_d = hubs[neighbor].max_drones
                if calendar.is_hub_available(neighbor, arrival_turn, n_max_d):
                    heapq.heappush(queue,
                                   (cost + move_cost, new_prio, arrival_turn,
                                    neighbor,
                                    path + [(arrival_turn, neighbor)]))

    return None
