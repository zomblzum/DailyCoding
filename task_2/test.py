import unittest
import array_multiplicator as am

class TestSearch(unittest.TestCase):
    def test_multiply(self):
        input_array = [1,2,3,4,5]
        result_array = [120,60,40,30,24]

        self.assertEqual(am.multiply(input_array), result_array)

        input_array = [3,2,1]
        result_array = [2,3,6]
    
        self.assertEqual(am.multiply(input_array), result_array)

if __name__ == '__main__':
    unittest.main()