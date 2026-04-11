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
#  Updated: 2026/04/11 09:54:38 by rruiz                                      #
# *************************************************************************** #

from sys import argv as av
from src.models.errors import ArgError, MapFileError
from src.parsing.parsing import Parser

def main():
    try:
        ac = len(av)
        if ac > 3:
            raise ArgError('Error, too many arguments.')

        fly_in = Parser(av[2])


    except (MapFileError, TypeError) as e:
        print(e)
    except Exception as e:
        print(f'Unexpected error, "{e}"')

if __name__ == "__main__":
    main()