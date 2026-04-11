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
#  Updated: 2026/04/11 17:57:09 by rruiz                                      #
# *************************************************************************** #

from enum import Enum

class ZoneType(Enum):
    """All zone types available.

    Attributes:
        NORMAL (str): Standard zone with 1 turn movement cost (default).
        BLOCKED (str): Inaccessible zone. Drones must not enter or pass through
            this zone. Any path using it is invalid.
        RESTRICTED (str): A sensitive or dangerous zone. Movement to this zone
            costs 2 turns.
        PRIORITY (str): A preferred zone. Movement to this zone costs 1 turn
            but should be prioritized in pathfinding.
    """
    NORMAL = 'normal'
    BLOCKED = 'blocked'
    RESTRICTED = 'restricted'
    PRIORITY = 'priority'

class Color(Enum):
    """Available ANSI escape sequences for terminal text formatting.

    Attributes:
        BLACK (str): Black color.
        BLUE (str): Blue color.
        BOLD (str): Applies bold formatting to the text.
        BROWN (str): Brown color.
        CYAN (str): Cyan color.
        DARK_GRAY (str): Dark gray color.
        END (str): Resets all text formatting and colors to terminal defaults.
        FAINT (str): Decreases text intensity.
        GREEN (str): Green color.
        ITALIC (str): Text in italics.
        LIGHT_BLUE (str): Light blue color.
        LIGHT_CYAN (str): Light cyan color.
        LIGHT_GRAY (str): Light gray color.
        LIGHT_GREEN (str): Light green color.
        LIGHT_PURPLE (str): Light purple color.
        LIGHT_RED (str): Light red color.
        LIGHT_WHITE (str): Light white color.
        PURPLE (str): Purple color.
        RED (str): Red color.
        UNDERLINE (str): Horizontal line over the text.
        YELLOW (str): Yellow color.
    """
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BROWN = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    LIGHT_GRAY = '\033[0;37m'
    DARK_GRAY = '\033[1;30m'
    LIGHT_RED = '\033[1;31m'
    LIGHT_GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    LIGHT_BLUE = '\033[1;34m'
    LIGHT_PURPLE = '\033[1;35m'
    LIGHT_CYAN = '\033[1;36m'
    LIGHT_WHITE = '\033[1;37m'
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'