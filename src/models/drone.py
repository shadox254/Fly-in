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
#  File: drone.py                                                             #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/04/13 08:58:51 by rruiz                                      #
#  Updated: 2026/05/15 10:07:11 by rruiz                                      #
# *************************************************************************** #

from src.models.hub import Hub

class Drone():
    '''Representation of a drone.

    Args:
        name (str): Unique identifier formatted as 'D' followed by the ID.
        current_zone (Hub): The hub where the drone is currently located.
        path (list[Hub]): Ordered sequence of hubs to visit.
        has_finish (bool): Status indicating if the drone has reached its destination.
    '''
    def __init__(self, id: int, start_zone: Hub):
        '''Initialize a new Drone instance.

        Args:
            id (int): Numerical ID used to generate the drone's name.
            start_zone (Hub): The initial hub where the drone starts.
        '''
        self.name = "D" + str(id)
        self.current_zone = start_zone
        self.path: list[Hub] = []
        self.has_finish = False
