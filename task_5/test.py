import unittest
import cons as c

class TestSearch(unittest.TestCase):
    def test_car(self):
        self.assertEqual(c.car(c.cons(3, 4)),3)

    def test_cdr(self):
        self.assertEqual(c.cdr(c.cons(3, 4)),4)

if __name__ == '__main__':
    unittest.main()