import unittest
from sum_searcher import *

class TestSearch(unittest.TestCase):
    def test_decode(self):
        array = [2,4,6,8]
        result = 12

        self.assertEqual(find_max_sum_of_non_adjacent(array),result)

        array = [5,1,1,5]
        result = 10

        self.assertEqual(find_max_sum_of_non_adjacent(array),result)
        
if __name__ == '__main__':
    unittest.main()