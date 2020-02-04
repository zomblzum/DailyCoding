import unittest
from unival_tree import *

class TestSearch(unittest.TestCase):
    def test_decode(self):
        f = Node(1)
        g = Node(1)
        e = Node(0)
        b = Node(1)
        d = Node(1, left=f, right=g)
        c = Node(0, left=d, right=e)
        a = Node(0, left=b, right=c)

        self.assertEqual(count_unival_trees(a), 5)

if __name__ == '__main__':
    unittest.main()