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
#  Updated: 2026/05/15 11:37:12 by rruiz                                      #
# *************************************************************************** #

class ReservationCalendar:
    '''A time-slotted registry for tracking resource occupancy.

    This class manages the availability of hubs and connections over
    turns to prevent collisions and over-capacity scenarios.

    Attributes:
        reservations (dict[tuple[int, str], int]): A mapping where the key
            is a tuple of (turn_number, resource_id) and the value is the
            count of drones currently occupying that resource.
    '''
    def __init__(self) -> None:
        '''Initialize an empty reservation calendar.'''
        self.reservations: dict[tuple[int, str], int] = {}

    def _get_connection_id(self, hub1_name: str, hub2_name: str) -> str:
        '''Generate a unique, sorted identifier for a link between two hubs.

        By sorting the names, it ensures that the connection (A, B) is
        treated the same as (B, A), making the graph undirected.

        Args:
            hub1_name (str): Name of the first hub.
            hub2_name (str): Name of the second hub.

        Returns:
            str: A string identifier formatted as 'hub_min-hub_max'.
        '''
        hubs = sorted([hub1_name, hub2_name])
        return f"{hubs[0]}-{hubs[1]}"

    def is_hub_available(self, hub_name: str, turn: int,
                         max_capacity: int) -> bool:
        '''Check if a hub has remaining capacity for a specific turn.

        Args:
            hub_name (str): The hub to verify.
            turn (int): The specific time step/turn.
            max_capacity (int): The maximum number of drones allowed on the
            hub.

        Returns:
            bool: True if occupancy is strictly less than max_capacity, False
            otherwise.
        '''
        current_occupancy = self.reservations.get((turn, hub_name), 0)
        if current_occupancy < max_capacity:
            return True
        else:
            return False

    def is_connection_available(self, hub1: str, hub2: str, turn: int,
                                max_capacity: int) -> bool:
        '''Check if a connection between two hubs can accept another drone
        for a specific turn.

        Args:
            hub1 (str): Name of the first hub.
            hub2 (str): Name of the second hub.
            turn (int): The specific time step/turn.
            max_capacity (int): The maximum capacity of the link.

        Returns:
            bool: True if the connection is not saturated, False otherwise.
        '''
        conn_id = self._get_connection_id(hub1, hub2)
        current_occupancy = self.reservations.get((turn, conn_id), 0)
        if current_occupancy < max_capacity:
            return True
        else:
            return False

    def reserve_hub(self, hub_name: str, turn: int) -> None:
        '''Increment the occupancy count of a hub for a given turn.

        Args:
            hub_name (str): The hub to reserve.
            turn (int): The specific time step/turn.
        '''
        key = (turn, hub_name)
        self.reservations[key] = self.reservations.get(key, 0) + 1

    def reserve_connection(self, hub1: str, hub2: str, turn: int) -> None:
        '''Increment the occupancy count of a connection for a given turn.

        Uses a canonical ID to ensure the reservation is bidirectional.

        Args:
            hub1 (str): Name of the first hub.
            hub2 (str): Name of the second hub.
            turn (int): The specific time step/turn.
        '''
        conn_id = self._get_connection_id(hub1, hub2)
        key = (turn, conn_id)
        self.reservations[key] = self.reservations.get(key, 0) + 1
