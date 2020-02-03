import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.both = id(data)

    def __repr__(self):
        return str(self.data)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

id_map = dict()
id_map[id("a")] = a
id_map[id("b")] = b
id_map[id("c")] = c
id_map[id("d")] = d
id_map[id("e")] = e

class XORLinkedList:
    def __init__(self,node):
        self.head = node
        self.tail = node
        self.head.both = 0
        self.tail.both = 0

    def add(self,element):
        self.tail.both ^= id(element.data)
        element.both = id(self.tail.data)
        self.tail = element

    def get(self,index):
        prev = 0
        result = self.head

        for i in range(index):
            next = prev ^ result.both
            prev = id(result.data)
            result = id_map[next]

        return result.data

class TestSearch(unittest.TestCase):
    def test_list(self):
        xor_list = XORLinkedList(c)
        xor_list.add(d)
        xor_list.add(e)
        xor_list.add(a)

        self.assertEqual(xor_list.get(0),"c")
        self.assertEqual(xor_list.get(1),"d")
        self.assertEqual(xor_list.get(2),"e")
        self.assertEqual(xor_list.get(3),"a")

if __name__ == '__main__':
    unittest.main()