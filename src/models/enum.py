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
#  File: enum.py                                                              #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/04/03 09:36:55 by rruiz                                      #
#  Updated: 2026/05/15 11:19:36 by rruiz                                      #
# *************************************************************************** #

from enum import Enum


class ZoneType(Enum):
    '''All zone types available.

    Args:
        NORMAL (str): Standard zone with 1 turn movement cost (default).
        BLOCKED (str): Inaccessible zone. Drones must not enter or pass through
            this zone. Any path using it is invalid.
        RESTRICTED (str): A sensitive or dangerous zone. Movement to this zone
            costs 2 turns.
        PRIORITY (str): A preferred zone. Movement to this zone costs 1 turn
            but should be prioritized in pathfinding.
    '''
    NORMAL = 'normal'
    BLOCKED = 'blocked'
    RESTRICTED = 'restricted'
    PRIORITY = 'priority'


class Color(Enum):
    '''Available ANSI escape sequences for terminal text formatting.

    Args:
        BLACK (str): Black color.
        BLUE (str): Blue color.
        BROWN (str): Brown color.
        CRIMSON (str): Crimson color.
        CYAN (str): Cyan color.
        DARKGRAY (str): Dark gray color.
        DARKRED (str): Dark red color.
        GOLD (str): Gold color.
        GREEN (str): Green color.
        LIGHTBLUE (str): Light blue color.
        LIGHTCYAN (str): Light cyan color.
        LIGHTGRAY (str): Light gray color.
        LIGHTGREEN (str): Light green color.
        LIGHTPURPLE (str): Light purple color.
        LIGHTRED (str): Light red color.
        LIME (str): Lime color.
        MAGENTA (str): Magenta color.
        MAROON (str): Maroon color.
        ORANGE (str): Orange color.
        PURPLE (str):  Purple color.
        RAINBOW (str): Hmm...
        RED (str): Red color.
        VIOLET (str): Violet color.
        YELLOW (str): Yellow color.
        RESET (str): Resets all text formatting and colors to terminal
            defaults.
    '''
    BLACK = 0
    BLUE = 4
    BROWN = 3
    CRIMSON = 160
    CYAN = 6
    DARKGRAY = 240
    DARKRED = 88
    GOLD = 214
    GREEN = 2
    LIGHTBLUE = 117
    LIGHTCYAN = 123
    LIGHTGRAY = 250
    LIGHTGREEN = 113
    LIGHTPURPLE = 98
    LIGHTRED = 203
    LIME = 118
    MAGENTA = 162
    MAROON = 196
    ORANGE = 202
    PURPLE = 5
    RED = 1
    VIOLET = 165
    YELLOW = 11
    RESET = 255
