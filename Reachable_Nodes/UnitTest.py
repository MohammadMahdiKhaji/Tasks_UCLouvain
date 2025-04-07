import unittest
from Reachable_Nodes.Main import reachable


class AdjacencyTestCase(unittest.TestCase):

    def testCase1(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        self.assertEqual(reachable(adj_list, 0), {0, 1, 2, 3, 4})

    def testCase2(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        self.assertEqual(reachable(adj_list, 3), {3, 4})

    def testCase3(self):
        adj_list = [[1, 2], [0, 3], [0], [1, 4], [3]]
        self.assertEqual(reachable(adj_list, 3), {0, 1, 2, 3, 4})

    def testCase4(self):
        adj_list = [[1, 2, 3, 4], [], [], [], []]
        self.assertEqual(reachable(adj_list, 0), {0, 1, 2, 3, 4})

if __name__ == '__main__':
    unittest.main()