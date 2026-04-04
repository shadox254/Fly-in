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
#  File: __main__.py                                                          #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/04/03 09:37:06 by rruiz                                      #
#  Updated: 2026/04/04 09:25:55 by rruiz                                      #
# *************************************************************************** #

from argparse import ArgumentParser

from sys import argv as av
from src import ArgError

def main():
    try:
        ac = len(av)
        if ac > 3:
            raise ArgError("Error, too many arguments.")

        arg = ArgumentParser()
        arg.add_argument(
            "--file", "-f",
            help="Path to the file containing the map",
            default="maps/easy/01_linear_path.txt",
            type=str
        )
        arg = arg.parse_args()

        with open(arg.file, "r"):
            pass

    except FileNotFoundError as e:
        print(f"Error, map not found: {e.filename}")
    except Exception as e:
        print(f"Unexpected error, {e}")

if __name__ == "__main__":
    main()