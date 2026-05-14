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
#  File: engine.py                                                            #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/05/13 09:35:57 by rruiz                                      #
#  Updated: 2026/05/14 14:29:13 by rruiz                                      #
# *************************************************************************** #

from src.models.calendar import ReservationCalendar
from src.algo.pathfinding import calculate_drone_path
from src.models.enum import Color

class Engine:
    def __init__(self, manager):
        self.manager = manager
        self.calendar = ReservationCalendar()
        self.paths = {}

    def calculate_all_paths(self):
        for drone in self.manager.drone_list:
            path = calculate_drone_path(
                self.manager.start_hub_name,
                self.manager.end_hub_name,
                0,
                self.calendar,
                self.manager.hubs,
                self.manager.connections
            )
            self.paths[drone.name] = path

            if path:
                for i in range(len(path)):
                    turn, hub = path[i]
                    self.calendar.reserve_hub(hub, turn)

                    if i > 0:
                        prev_turn, prev_hub = path[i - 1]
                        for t in range(prev_turn + 1, turn + 1):
                            self.calendar.reserve_connection(prev_hub, hub, t)

    def _get_original_connection_name(self, hub1, hub2):
        search_key = f"{hub1}-{hub2}"
        return self.manager.connection_names.get(search_key, search_key)

    def _get_drone_state(self, path, turn):
        if not path:
            return None

        if turn < path[0][0]:
            return None

        if turn >= path[-1][0]:
            return path[-1][1]

        for i in range(len(path) - 1):
            t1, hub1 = path[i]
            t2, hub2 = path[i + 1]

            if turn == t1:
                return hub1
            if t1 < turn < t2:
                return (hub1, hub2)

        return None

    def simulate(self):
        max_turn = 0
        for path in self.paths.values():
            if path:
                max_turn = max(max_turn, path[-1][0])

        for current_turn in range(1, max_turn + 1):
            turn_output = []

            for drone in self.manager.drone_list:
                path = self.paths.get(drone.name)
                if not path:
                    continue

                current_state = self._get_drone_state(path, current_turn)
                prev_state = self._get_drone_state(path, current_turn - 1)

                if current_state and current_state != prev_state:
                    if isinstance(current_state, tuple):
                        conn_name = self._get_original_connection_name(current_state[0], current_state[1])
                        parts = conn_name.split('-')
                        colored_parts = []
                        
                        for part in parts:
                            hub_color_str = self.manager.hubs[part].color
                            try:
                                color_code = Color[hub_color_str.upper()].value
                            except KeyError:
                                color_code = Color.LIGHTGRAY.value
                            colored_parts.append(f"{color_code}{part}{Color.RESET.value}")
                            
                        colored_conn = "-".join(colored_parts)
                        turn_output.append(f"{drone.name}-{colored_conn}")
                    else:
                        hub_color_str = self.manager.hubs[current_state].color
                        try:
                            color_code = Color[hub_color_str.upper()].value
                        except KeyError:
                            color_code = Color.LIGHTGRAY.value
                        turn_output.append(f"{drone.name}-{color_code}{current_state}{Color.RESET.value}")

            if turn_output:
                print(" ".join(turn_output))
