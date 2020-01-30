import unittest
from btree import *

class TestSearch(unittest.TestCase):
    def test_both(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        assert deserialize(serialize(node)).left.left.val == 'left.left'

if __name__ == '__main__':
    unittest.main()