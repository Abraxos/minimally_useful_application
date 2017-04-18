'''The core of the minimally useful application, has main function.'''
from .timing import timing
from .utils.config_utils import create_default_config_ifndef, load_configuration
from .utils.config_utils import DEFAULT_CONFIG_PATH
from .utils.cli_utils import process_arguments

def main():
    '''Loads the configuration file, parses commandline arguments,
       and outputs the current time.'''
    args = process_arguments()
    config_path = DEFAULT_CONFIG_PATH if not args.configuration else \
                  args.configuration
    create_default_config_ifndef(config_path)
    config = load_configuration(config_path)

    current_time = timing.get_current_time()
    print(timing.convert_time_to(current_time,
          config[timing.SECTION]['timezone']))

if __name__ == '__main__':
    main()
