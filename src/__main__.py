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
#  Updated: 2026/05/15 11:10:33 by rruiz                                      #
# *************************************************************************** #

from sys import argv as av
from src.models.errors import ArgError, MapFileError
from src.parsing.parsing import Parser
from src.simulation.engine import Engine


def main():
    '''Main entry point of the program.

    Retrieves command-line arguments to determine the map file to parse.
    Initializes the parser, configures the simulation engine, calculates the
    drone paths, and starts the execution.

    Catches known errors (MapFileError, TypeError) for clean output, and
    intercepts unexpected errors by walking through the traceback to identify
    the specific file and line of the crash.
    '''
    try:
        ac = len(av)
        if ac == 3 and av[1] == '--file':
            map_file = av[2]
        elif ac == 2:
            map_file = av[1]
        else:
            raise ArgError('Error, bad arguments.')

        p = Parser(map_file)

        engine = Engine(p.manager)
        engine.calculate_all_paths()
        engine.simulate()

    except (MapFileError, TypeError) as e:
        print(e)
    except Exception as e:
        tb = e.__traceback__
        while tb.tb_next:
            tb = tb.tb_next

        file = tb.tb_frame.f_code.co_filename
        function = tb.tb_frame.f_code.co_name
        line = tb.tb_lineno

        print(f'Unexpected error, "{e}"\nin: {file}\nfunction: {function},'
              f' line: {line}')


if __name__ == "__main__":
    main()
