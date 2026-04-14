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
#  Updated: 2026/04/14 17:59:40 by rruiz                                      #
# *************************************************************************** #

from sys import argv as av
from src.models.errors import ArgError, MapFileError
from src.parsing.parsing import Parser

def main():
    try:
        ac = len(av)
        if ac != 3:
            raise ArgError('Error, too many arguments.')

        p = Parser(av[2])
        manager = p.manager
        print(p.manager.hubs)
        for drone in manager.drone_list:
            print(drone.name)

    except (MapFileError, TypeError) as e:
        print(e)
    except Exception as e:
        tb = e.__traceback__
        while tb.tb_next:
            tb = tb.tb_next

        file = tb.tb_frame.f_code.co_filename
        function = tb.tb_frame.f_code.co_name
        line = tb.tb_lineno
        
        print(f'Unexpected error, "{e}"'
              f'\nin: {file}\nfunction: {function}, line: {line}')

if __name__ == "__main__":
    main()