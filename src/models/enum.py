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
#  Updated: 2026/05/13 09:46:26 by rruiz                                      #
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
        BROWN (str): Brown color.
        CRIMSON (str): Crimson color.
        CYAN (str): Cyan color.
        DARKGRAY (str): Dark gray color.
        DARKRED (str): Dark red color.
        GOLD (str): Gold color.
        GREEN (str): Green color.
        LIGHTRED (str): Light red color.
        LIGHTBLUE (str): Light blue color.
        LIGHTCYAN (str): Light cyan color.
        LIGHTGRAY (str): Light gray color.
        LIGHTGREEN (str): Light green color.
        LIGHTPURPLE (str): Light purple color.
        LIGHTWHITE (str): Light white color.
        LIME (str): Lime color.
        MAGENTA (str): Magenta color.
        MAROON (str): Maroon color.
        ORANGE (str): Orange color.
        PURPLE (str):  Purple color.
        RAINBOW (str): Hmm...
        RED (str): Red color.
        VIOLET (str): Violet color.
        YELLOW (str): Yellow color.

        BOLD (str): Applies bold formatting to the text.
        FAINT (str): Decreases text intensity.
        ITALIC (str): Text in italics.
        UNDERLINE (str): Horizontal line over the text.
        RESET (str): Resets all text formatting and colors to terminal
            defaults.
    """
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BROWN = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    LIGHTGRAY = '\033[0;37m'
    DARKGRAY = '\033[1;30m'
    LIGHTRED = '\033[1;31m'
    LIGHTGREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    LIGHTBLUE = '\033[1;34m'
    LIGHTPURPLE = '\033[1;35m'
    LIGHTCYAN = '\033[1;36m'
    LIGHTWHITE = '\033[1;37m'
    ORANGE = '\033[38;5;214m'
    MAROON = '\033[38;5;52m'
    GOLD = '\033[38;5;220m'
    DARKRED = '\033[38;5;88m'
    VIOLET = '\033[38;5;177m'
    CRIMSON = '\033[38;5;161m'
    LIME = '\033[38;5;118m'
    MAGENTA = '\033[38;5;201m'
    RAINBOW = '\033[0m' # don't know how to do...
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'