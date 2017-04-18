'''Timing functionality'''
from arrow import utcnow

SECTION = 'Timing Information'

def get_current_time():
    '''Returns the current time in a given locale'''
    return utcnow()

def convert_time_to(time, timezone_string):
    '''Converts a given time to a given locale'''
    return time.to(timezone_string)
