'''Tests for the timing submodule'''
import unittest
from ..timing import get_current_time, convert_time_to

class TestTimingMethods(unittest.TestCase):
    '''A test case for verifying the timing methods'''

    def test_get_current_time(self):
        '''Confirms that the get_current_time function works as expected.'''
        self.assertNotEqual(get_current_time(), get_current_time())

    def test_convert_time_to(self):
        '''Confirms that the convert_time_to function is working as expected.'''
        time = get_current_time()
        expected_time = time.to('US/Eastern')
        self.assertEqual(expected_time, convert_time_to(time, 'US/Eastern'))

if __name__ == '__main__':
    unittest.main()
