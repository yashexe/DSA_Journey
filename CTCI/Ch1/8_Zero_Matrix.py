# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

import unittest
#-------------------------------------------------------------

def zero_matrix(matrix):
    zero_row = False
    columns = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_row = True
                if j not in columns:
                    columns.append(j)

        if zero_row:
            zero_row = False
            matrix[i] = [0 for _ in range(len(matrix[0]))]
        
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j in columns:
                matrix[i][j] = 0

    return matrix

#-------------------------------------------------------------
# Time: O(MN) - need to find zeros before setting matrix
# Space: O(N) - worst case all columns have a 0, rows are determined at the end of each column sweep, by a bln value
#-------------------------------------------------------------

class test(unittest.TestCase):
    def test_zero_matrix(self):
        answer = zero_matrix([[0,0],[0,0]])
        expected = [[0,0],[0,0]]
        self.assertEqual(answer, expected)

    def test_only_one_row(self):
        answer = zero_matrix([[1,2,3,4,0]])
        expected = [[0,0,0,0,0]]
        self.assertEqual(answer, expected)
    def test_only_one_col(self):
        answer = zero_matrix([[1],[2],[3],[4],[0]])
        expected = [[0],[0],[0],[0],[0]]
        self.assertEqual(answer, expected)

    def test_full_matrix(self):
        answer = zero_matrix([[7,8,9],[1,2,3],[4,5,6],[7,9,8]])
        expected = [[7,8,9],[1,2,3],[4,5,6],[7,9,8]]
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()