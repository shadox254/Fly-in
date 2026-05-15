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
#  File: manager.py                                                           #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/04/04 10:38:36 by rruiz                                      #
#  Updated: 2026/05/15 11:22:27 by rruiz                                      #
# *************************************************************************** #

from src.models.hub import Hub
from src.models.drone import Drone
from src.models.enum import ZoneType, Color
from src.models.errors import StartHubError, EndHubError


class FlyinManager():
    '''Representation of the manager.

    Args:
        hubs (dict[str, Hub]): Dictionnary where key are hubs name and value
            are the Hub with their informations.
        drone_nbr (int): The number of drones.
        has_start (int): Like a boolean: true if there is a start,
            false otherwise.
        has_end (int): Like a boolean: true if there is a end, false otherwise.
        start_hub_name (str): The name of the starting hub.
        end_hub_name (str): The name of the ending hub
        connections (dict[str, dict[str, int]]): Adjacency map representing
        the graph.
            - Key (str): Source hub name.
            - Value (dict): Neighbors where Key is destination and Value is
                capacity link.
        connection_names (dict[str, str]): Normalization map for links.
            Maps both 'A-B' and 'B-A' to a single connection string.
        drone_list (list): List of all existing drones.
    '''
    def __init__(self, drone_nbr: int):
        '''Initialize the manager with a specific number of drones.

        Args:
            drone_nbr (int): The total number of drones to manage in the
                simulation.
        '''
        self.hubs = {}
        self.drone_nbr = drone_nbr
        self.has_start = 0
        self.has_end = 0
        self.start_hub_name = ""
        self.end_hub_name = ""
        self.connections = {}
        self.connection_names = {}
        self.drone_list = []

    def add_hub(self, informations_line: str):
        '''Parse a configuration line to create and store a new Hub.

        This method handles start, end, and normal hubs, parsing their
        coordinates and optional metadata (zone, color, max_drones).

        Args:
            informations_line (str): A raw string containing hub
                specifications.

        Raises:
            StartHubError: If more than one start hub is defined.
            EndHubError: If more than one end hub is defined.
            TypeError: If an unknown metadata tag is encountered.
        '''
        parts = informations_line.split('[')
        infos = parts[0].split()
        hub_type = infos[0]

        if hub_type == 'start_hub:':
            if not self.has_start:
                self.has_start = 1
                self.start_hub_name = infos[1]
            else:
                raise StartHubError('Error, too many start_hub in map')

        if hub_type == 'end_hub:':
            if not self.has_end:
                self.has_end = 1
                self.end_hub_name = infos[1]
            else:
                raise EndHubError('Error, too many end_hub in map')

        name = infos[1]
        x = int(infos[2])
        y = int(infos[3])

        zone = ZoneType.NORMAL.value
        color = Color.LIGHTGRAY

        if hub_type in ('start_hub:', 'end_hub:'):
            max_drones = self.drone_nbr
        else:
            max_drones = 1

        if len(parts) > 1:
            metadata_str = parts[1].replace(']', '').strip()
            tags = metadata_str.split()

            for tag in tags:
                curr_value = tag.split('=')
                if len(curr_value) != 2:
                    continue

                match curr_value[0]:
                    case 'zone':
                        zone = curr_value[1]
                    case 'color':
                        color = curr_value[1]
                    case 'max_drones':
                        if hub_type not in ('start_hub:', 'end_hub:'):
                            max_drones = int(curr_value[1])
                    case _:
                        raise TypeError('Error, invalid metadata "'
                                        f'{curr_value[0]}"')

        self.hubs[name] = Hub(name, x, y, [], zone, color, max_drones)

    def add_connection(self, connection_line: str):
        '''Parse a connection line to establish a link between two hubs.
            Updates the adjacency map. Connections are bidirectional with
            a defined capacity.

        Args:
            connection_line (str): A raw string containing the connection
                link (e.g., "connection: H1-H2 [max_link_capacity=2]").
        '''
        parts = connection_line.split('[')
        infos = parts[0].replace('connection:', '').strip()
        hub_names = infos.split('-')

        if len(hub_names) != 2:
            return

        hub1_name = hub_names[0].strip()
        hub2_name = hub_names[1].strip()
        hub1 = self.hubs.get(hub1_name)
        hub2 = self.hubs.get(hub2_name)

        if not hub1 or not hub2:
            return

        capacity = 1
        if len(parts) > 1:
            metadata = parts[1].replace(']', '').strip()
            for tag in metadata.split():
                if 'max_link_capacity=' in tag:
                    capacity = int(tag.split('=')[1])

        self.connections.setdefault(hub1_name, {})[hub2_name] = capacity
        self.connections.setdefault(hub2_name, {})[hub1_name] = capacity

        original_name = f"{hub1_name}-{hub2_name}"
        self.connection_names[f"{hub1_name}-{hub2_name}"] = original_name
        self.connection_names[f"{hub2_name}-{hub1_name}"] = original_name

    def create_drones(self):
        '''Instantiate drones based on the drone_nbr and place them on the
            start hub.

        Populates the drone_list with new Drone objects, each assigned a
            unique name based on its incremented ID.
        '''
        start_zone = self.hubs[self.start_hub_name]
        for id in range(self.drone_nbr):
            drone = Drone(id + 1, start_zone)
            self.drone_list.append(drone)
