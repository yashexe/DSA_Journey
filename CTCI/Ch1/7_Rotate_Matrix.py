# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# eg.
# matrix[rows[columns]
# 1  2  3  4    13 9  5 1  30, 20, 10, 00
# 5  6  7  8    14 10 6 2
# 9  10 11 12   15 11 7 3
# 13 14 15 16   16 12 8 4

import unittest
#-------------------------------------------------------------

def Rotate_Matrix(matrix):
    if len(matrix) == 1:
        return matrix
 
    for first in range(len(matrix) // 2):
        last = len(matrix) - 1 - first
        
        for column in range(first,last):

            top = matrix[first][column]

            matrix[first][column] = matrix[-column - 1][first]

            matrix[-column - 1][first] = matrix[last][-column - 1]

            matrix[last][-column - 1] = matrix[column][last]

            matrix[column][last] = top
    return matrix

#-------------------------------------------------------------
# Time: O(n^2)
# Space: O(1) - no additional DS that scale with input size
#-------------------------------------------------------------

class test(unittest.TestCase):
    def test_single(self):
        answer = Rotate_Matrix([[4]])
        expected = [[4]]
        self.assertEqual(answer, expected)

    def test_even(self):
        answer = Rotate_Matrix([[1,2],[3,4]])
        expected = [[3,1],[4,2]]
        self.assertEqual(answer, expected)

    def test_odd(self):
        answer = Rotate_Matrix([[1,2,3],[4,5,6],[7,8,9]])
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        self.assertEqual(answer, expected)

if __name__ == '__main__':
    unittest.main()