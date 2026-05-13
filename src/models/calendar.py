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
#  File: calendar.py                                                          #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/05/13 09:35:30 by rruiz                                      #
#  Updated: 2026/05/13 09:35:33 by rruiz                                      #
# *************************************************************************** #

class ReservationCalendar:
    def __init__(self):
        self.reservations = {}

    def _get_connection_id(self, hub1_name: str, hub2_name: str) -> str:
        hubs = sorted([hub1_name, hub2_name])
        return f"{hubs[0]}-{hubs[1]}"

    def is_hub_available(self, hub_name: str, turn: int, max_capacity: int) -> bool:
        current_occupancy = self.reservations.get((turn, hub_name), 0)
        return current_occupancy < max_capacity

    def is_connection_available(self, hub1: str, hub2: str, turn: int, max_capacity: int) -> bool:
        conn_id = self._get_connection_id(hub1, hub2)
        current_occupancy = self.reservations.get((turn, conn_id), 0)
        return current_occupancy < max_capacity

    def reserve_hub(self, hub_name: str, turn: int):
        key = (turn, hub_name)
        self.reservations[key] = self.reservations.get(key, 0) + 1

    def reserve_connection(self, hub1: str, hub2: str, turn: int):
        conn_id = self._get_connection_id(hub1, hub2)
        key = (turn, conn_id)
        self.reservations[key] = self.reservations.get(key, 0) + 1