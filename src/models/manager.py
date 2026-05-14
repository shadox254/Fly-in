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
#  Updated: 2026/05/14 14:59:44 by rruiz                                      #
# *************************************************************************** #

from src.models.hub import Hub
from src.models.drone import Drone
from src.models.enum import ZoneType, Color
from src.models.errors import StartHubError, EndHubError

class FlyinManager():
    def __init__(self, drone_nbr: int):
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
                self.has_end += 1
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
        start_zone = self.hubs[self.start_hub_name]
        for id in range(self.drone_nbr):
            drone = Drone(id + 1, start_zone)
            self.drone_list.append(drone)