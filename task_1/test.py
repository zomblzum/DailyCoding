import unittest
import sum_searcher as ss

class TestSearch(unittest.TestCase):
    def test_search(self):
        some_array = [10, 15, 3, 7]
        some_result = 17

        self.assertTrue(ss.list_contain_equal_sum(some_array, some_result))

    def test_search_with_duplicates(self):
        some_array = [10, 15, 3, 7, 10]
        some_result = 20

        self.assertTrue(ss.list_contain_equal_sum(some_array, some_result))

if __name__ == '__main__':
    unittest.main()