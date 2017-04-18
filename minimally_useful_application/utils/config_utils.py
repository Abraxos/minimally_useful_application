'''Common utility functions for configuration'''
import os
import configparser

# Local package imports
from .file_utils import create_filepath

DEFAULT_CONFIG_PATH = os.path.expanduser('~/.config/minimally_useful_\
                                          application/config.ini')

def load_configuration(config_path):
    '''Loads a given configuration file'''
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def default_config():
    '''Produces a configuration object that would be equivalent to
       the following config.ini file:

       [Timing Information]
       timezone = US/Eastern'''
    config = configparser.ConfigParser()
    config['Timing Information'] = {'timezone' : 'US/Eastern'}
    return config


def create_default_config_ifndef(config_path):
    '''Creates a default configuration file if one does not exist.'''
    if not os.path.isfile(config_path):
        create_filepath(config_path)
        with open(config_path, 'w') as configfile:
            default_config().write(configfile)
