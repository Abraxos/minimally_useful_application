'''File utility functions'''
import os

def create_filepath(filepath, contents=''):
    '''Creates a file and all ancestor directories if they do not exist,
       optionally with contents.'''
    def new_file_with_contents(contents):
        '''Creates a new file with the given contents'''
        with open(filepath, 'w+') as file_to_create:
            file_to_create.write(contents)
    if os.path.isdir(os.path.dirname(filepath)):
        if not os.path.isfile(filepath):
            new_file_with_contents(contents)
    else:
        parent_dir = os.path.dirname(filepath)
        if parent_dir:
            os.makedirs(parent_dir)
        new_file_with_contents(contents)
