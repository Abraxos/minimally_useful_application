'''Common utilities for command-line interfaces and arguments'''
import argparse
import os

class ReadableDir(argparse.Action): # pylint: disable=R0903
    '''A highly useful class that serves as an example of how one can abstract
       the verification of commandline arguments. Specifically, this class
       verifies that a given directory exists and is readable. It can be used
       like so:
           arg_parser.add_argument('--input_directory', action=ReadableDir)'''
    def __call__(self, parser, namespace, prospective_dir, option_string=None):
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace, self.dest, prospective_dir)
        else:
            raise argparse.ArgumentTypeError("{} is either not readable or \
                                              does not exist"
                                             .format(prospective_dir))

class WriteableDir(argparse.Action): # pylint: disable=R0903
    '''A highly useful class that serves as an example of how one can abstract
       the verification of commandline arguments. Specifically, this class
       verifies that a given directory exists and is write-able. It can be used
       like so:
           arg_parser.add_argument('--input_directory', action=WriteableDir)'''
    def __call__(self, parser, namespace, prospective_dir, option_string=None):
        if os.access(prospective_dir, os.W_OK):
            setattr(namespace, self.dest, prospective_dir)
        else:
            raise argparse.ArgumentTypeError("{} is either not write-able or \
                                              does not exist"
                                             .format(prospective_dir))

def process_arguments():
    '''Parses arguments from the commandline and initializes the argparser'''
    arg_parser = argparse.ArgumentParser(description='A script that prints out the time')
    arg_parser.add_argument('configuration', type=str, nargs='?',
                            help='Optional configuration file.')
    args = arg_parser.parse_args()
    return args
