import unittest
import searcher as s

class TestSearch(unittest.TestCase):
    def test_searc(self):
        input_array = [3, 4, -1, 1]
        result = 2

        self.assertEqual(s.find_lowest_positive_missing_integer_in_array(input_array), result)

        input_array = [1, 2, 0]
        result = 3

        self.assertEqual(s.find_lowest_positive_missing_integer_in_array(input_array), result)

if __name__ == '__main__':
    unittest.main()