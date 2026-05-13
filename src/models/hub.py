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
#  Updated: 2026/05/13 09:35:49 by rruiz                                      #
# *************************************************************************** #

from src.models.enum import ZoneType, Color

class Hub():
    def __init__(self, name: str, x: int, y: int, connections: dict[str, int], type: str = ZoneType.NORMAL, color: str = Color.LIGHTGRAY, max_drones: str = 1):
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