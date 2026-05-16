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
#  Updated: 2026/05/16 11:58:33 by rruiz                                      #
# *************************************************************************** #

from src.models.errors import MapFileError, MapInfosError
from src.models.manager import FlyinManager


class Parser():
    '''Responsible for loading, validating, and parsing the map file.

    This class acts as a factory that initializes and populates a
    FlyinManager instance based on the provided map file's content.

    Attributes:
        map (str): The path to the map configuration file.
        manager (FlyinManager | None): The manager instance being built.
    '''
    def __init__(self, map: str) -> None:
        '''Initialize the Parser and trigger the parsing process.

        Args:
            map (str): Path to the map file to be processed.

        Raises:
            MapFileError: If the file cannot be accessed.
            MapInfosError: If the map content is logically invalid.
        '''
        self.map = map
        self.manager: FlyinManager | None = None

        self._file_is_valid()
        self._read_lines()

    def _file_is_valid(self) -> None:
        '''Perform low-level filesystem checks on the target map file.

        Verifies existence, permissions, and path integrity before reading.

        Raises:
            MapFileError: If any filesystem-related issue occurs.
        '''
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
            raise MapFileError(f'Error, path to the file is incorrect: '
                               f'"{file}"')

    def _read_lines(self) -> FlyinManager:
        '''Iterate through the map file and populate the manager.

        This method handles the logical sequence of the map file:
        1. Ignore comments and empty lines.
        2. Initialize the FlyinManager with drone count.
        3. Add hubs and establish connections.
        4. Validate final simulation requirements (start/end points).

        Returns:
            FlyinManager: The fully initialized manager ready for simulation.

        Raises:
            MapInfosError: If the file structure is invalid, the manager is
                uninitialized, or mandatory hubs (start/end) are missing.
        '''
        with open(self.map, 'r') as f:
            for line in f:
                line = line.split("#")[0].strip()
                if not line:
                    continue

                if line.startswith('nb_drones'):
                    try:
                        drone_nbr = int(line.split(":")[1])
                        if drone_nbr <= 0:
                            raise MapInfosError('Error, nb_drones must be a '
                                                'positive integer')
                        self.manager = FlyinManager(drone_nbr)
                    except (ValueError, IndexError):
                        raise MapInfosError('Error, invalid nb_drones')

                elif line.startswith(('start_hub', 'hub', 'end_hub')):
                    if self.manager is None:
                        raise MapInfosError('Error, manager not '
                                            'initialized')
                    self.manager.add_hub(line)

                elif line.startswith('connection'):
                    if self.manager is None:
                        raise MapInfosError('Error, manager not '
                                            'initialized')
                    self.manager.add_connection(line)

                else:
                    raise MapInfosError(f'Error, map line invalid: '
                                        f'"{line}"')
        if self.manager is None:
            raise MapInfosError('Error, empty map')
        if self.manager.has_start != 1 or self.manager.has_end != 1:
            raise MapInfosError('Error, invalid number of start_hub or '
                                'end_hub')

        self.manager.create_drones()
        return self.manager
