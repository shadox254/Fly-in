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
#  Updated: 2026/04/14 18:00:17 by rruiz                                      #
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
        self.connections = {}
        self.drone_list = []

        self._create_drones()

    def add_hub(self, informations_line: str):
        parts = informations_line.split('[')
        infos = parts[0].split()

        if infos[0] == 'start_hub:':
            if not self.has_start:
                self.has_start = 1
            else:
                raise StartHubError('Error, too many start_hub in map')

        if infos[0] == 'end_hub:':
            if not self.has_end:
                self.has_end += 1
            else:
                raise EndHubError('Error, too many end_hub in map')

        name = infos[1]
        x = int(infos[2])
        y = int(infos[3])

        zone = ZoneType.NORMAL.value
        color = Color.LIGHT_GRAY
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
                        max_drones = int(curr_value[1])
                    case _:
                        raise TypeError(f'Error, invalid metadata "{curr_value[0]}"')

        self.hubs[name] = Hub(name, x, y, [], zone, color, max_drones)


    def add_connection(self, connection_line: str):
        parts = connection_line.split('[')
        infos = parts[0].replace('connection:', '').strip()
        hub_names = infos.split('-')

        if len(hub_names) != 2:
            return

        hub1_name = hub_names[0].strip()
        hub2_name = hub_names[1].strip()
        hub1 = self.hubs[hub1_name]
        hub2 = self.hubs[hub2_name]

        if not hub1 or not hub2:
            return

        capacity = 1
        if len(parts) > 1:
            metadata = parts[1].replace(']', '').strip()
            for tag in metadata.split():
                if 'max_link_capacity=' in tag:
                    capacity = int(tag.split('=')[1])

        self.connections.setdefault(hub1_name, {})[hub2_name] = capacity
        self.connections.setdefault(hub2_name, {})[hub1_name]= capacity


    def _create_drones(self):
        start_zone = self.hubs['start']
        for id in range(self.drone_nbr - 1):
            drone = Drone(id, start_zone)
            drone
            self.drone_list.append(drone)
