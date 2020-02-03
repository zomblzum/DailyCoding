import unittest
import decode_counter as c

class TestSearch(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(c.get_message_count(81),1)
        self.assertEqual(c.get_message_count(11),2)
        self.assertEqual(c.get_message_count(111),3)
        self.assertEqual(c.get_message_count(1111),5)
        self.assertEqual(c.get_message_count(1311),4)

if __name__ == '__main__':
    unittest.main()