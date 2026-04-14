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
#  File: parsing.py                                                           #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/04/03 11:11:38 by rruiz                                      #
#  Updated: 2026/04/14 17:55:43 by rruiz                                      #
# *************************************************************************** #

from src.models.errors import MapFileError, MapInfosError
from src.models.manager import FlyinManager

class Parser():
    def __init__(self, map: str) -> None:
        self.map = map
        self.manager = None

        self._file_is_valid()
        self._read_lines()

    def _file_is_valid(self):
        try:
            file = self.map
            with open(file, 'r'):
                pass
        except FileNotFoundError:
            raise MapFileError(f'Error, file not found: "{file}"')
        except PermissionError:
            raise MapFileError('Error, insufficient permissions to open '
                               f'file: "{file}"')
        except IsADirectoryError:
            raise MapFileError(f'Error, "{file}" is a directory')
        except NotADirectoryError:
            raise MapFileError(f'Error, path to the file is incorrect: "{file}"')

    def _read_lines(self) -> FlyinManager:
        try:
            with open(self.map, 'r') as f:
                for line in f:
                    if line.startswith('#') or line == '\n':
                        pass
                    elif line.startswith('nb_drones'):
                        self.manager = FlyinManager(int(line.split(":")[1]))
                    elif line.startswith(('start_hub', 'hub', 'end_hub')):
                        self.manager.add_hub(line)
                    elif line.startswith('connection'):
                        self.manager.add_connection(line)
                    else:
                        raise MapInfosError(f'Error, map line invalid: "{line}"')
        except ValueError:
            raise MapInfosError('Error, invalid nb_drones in map')
        if self.manager.has_start != 1 or self.manager.has_end != 1:
            print(self.manager.has_start, self.manager.has_end)
            raise MapInfosError('Error, invalid number of start_hub or end_hub')
        return self.manager