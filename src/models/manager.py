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
#  Updated: 2026/04/11 15:39:40 by rruiz                                      #
# *************************************************************************** #

from src.models.hub import Hub
from src.models.enum import ZoneType, Color
from src.models.errors import StartHubError, EndHubError

class FlyinManager():
    def __init__(self, drone_nbr: int):
        self.hub_list: list[Hub] = []
        self.drone_nbr = drone_nbr
        self.has_start = 0
        self.has_end = 0

    def add_hub(self, informations_line: str):
        parts = informations_line.split('[')
        infos = parts[0].split()

        if infos[0] == 'start_hub':
            if not self.has_start:
                self.has_start = 1
            else:
                raise StartHubError('Error, too many start_hub in map')

        if infos[0] == 'end_hub':
            if not self.has_end:
                self.has_end += 1
            else:
                raise EndHubError('Error, too many end_hub in map')

        name = infos[1]
        x = int(infos[2])
        y = int(infos[3])

        zone = ZoneType.NORMAL
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

        self.hub_list.append(Hub(name, x, y, [], zone, color, max_drones))


    def add_connection(self, connection_line: str):
        parts = connection_line.split('[')
        core_info = parts[0].replace('connection:', '').strip()
        hub_names = core_info.split('-')

        if len(hub_names) != 2:
            return

        name1, name2 = hub_names[0].strip(), hub_names[1].strip()

        # Recherche des objets Hub
        hub1 = next((h for h in self.hub_list if h.name == name1), None)
        hub2 = next((h for h in self.hub_list if h.name == name2), None)

        if not hub1 or not hub2:
            return

        capacity = 1
        if len(parts) > 1:
            metadata = parts[1].replace(']', '').strip()
            for tag in metadata.split():
                if 'max_link_capacity=' in tag:
                    capacity = int(tag.split('=')[1])

        hub1.connections[name2] = capacity
        hub2.connections[name1] = capacity
