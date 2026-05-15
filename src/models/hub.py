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
#  File: hub.py                                                               #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/04/04 10:41:53 by rruiz                                      #
#  Updated: 2026/05/15 10:07:11 by rruiz                                      #
# *************************************************************************** #

from src.models.enum import ZoneType, Color

class Hub():
    '''Representation of a hub.

    Args:
        name (str): Unique identifier of the hub.
        x (int): Horizontal coordinate on the grid.
        y (int): Vertical coordinate on the grid.
        zone_type (str): Type of hub.
        color (str): Name color for visual representation.
        max_drones (int): Capacity limit for simultaneous drones on this hub.
        connections (dict[str, int]): Map of reachable hub names and their travel costs.
    '''
    def __init__(self, name: str, x: int, y: int, connections: dict[str, int], type: str = ZoneType.NORMAL, color: str = Color.LIGHTGRAY, max_drones: str = 1):
        '''Initialize a new Hub instance.

        Args:
            name (str): Name of the hub.
            x (int): X-axis position.
            y (int): Y-axis position.
            connections (dict[str, int]): Dictionary where keys are neighbor names 
                and values are the path costs.
            type (str): Categorization of the hub. Defaults to ZoneType.NORMAL.
            color (str): Hub color. Defaults to Color.LIGHTGRAY.
            max_drones (int): Maximum capacity. Defaults to 1.

        Raises:
            TypeError: If the provided type is not a valid ZoneType.
        '''
        self.name = name
        zonetype_list = [s.value for s in ZoneType]
        if type not in zonetype_list:
            zonetype_str = ', '.join(map(str, zonetype_list[:-1])) + ' or ' + zonetype_list[-1]
            raise TypeError(f'Error, invalid zone type: {type}, type must be {zonetype_str}')

        self.x = x
        self.y = y
        self.zone_type = type
        self.color = color
        self.max_drones = max_drones
        self.connections = connections