import unittest
from Adjacency_Matrix_to_Adjacency_List.Main import mat_to_list


class AdjacencyTestCase(unittest.TestCase):

    def testCase1(self):
        adj_mat = [[0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0]]

        self.assertEqual(mat_to_list(adj_mat), [[1, 3], [2], [0], [4], [3], []])

    def testCase2(self):
        adj_mat = [[1, 1, 1, 0],
                   [1, 0, 0, 0],
                   [1, 0, 0, 0],
                   [0, 0, 0, 0]]
        self.assertEqual(mat_to_list(adj_mat), [[0, 1, 2], [0], [0], []])

    def testCase3(self):
        adj_mat = [[0, 0, 1, 1, 0],
                   [0, 1, 0, 1, 1],
                   [1, 0, 0, 0, 0],
                   [1, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
        self.assertEqual(mat_to_list(adj_mat), [[2, 3], [1, 3, 4], [0], [0, 1], [1]])

if __name__ == '__main__':
    unittest.main()