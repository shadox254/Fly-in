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
#  File: errors.py                                                            #
#  By: rruiz <rruiz@student.42.fr>                                            #
#  Created: 2026/04/03 11:29:03 by rruiz                                      #
#  Updated: 2026/05/15 11:19:51 by rruiz                                      #
# *************************************************************************** #

class ArgError(Exception):
    '''Exception raised for arguments errors.'''
    pass


class MapFileError(Exception):
    '''Exception raised for map file errors.'''
    pass


class MapInfosError(Exception):
    '''Exception raised for map informations errors.'''
    pass


class StartHubError(Exception):
    '''Exception raised for start hub errors.'''
    pass


class EndHubError(Exception):
    '''Exception raised for end hub errors.'''
    pass
