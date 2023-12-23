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
    for row in range(len(matrix) // 2):
        first = row
        last = len(matrix) - 1 - row
        
        for column in range(first,last):

            top = matrix[first][column]

            matrix[first][column] = matrix[-column - 1][first]

            matrix[-column - 1][first] = matrix[last][-column - 1]

            matrix[last][-column - 1] = matrix[column][last]

            matrix[column][last] = top
    return matrix

real = Rotate_Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
for i in range(len(real)):
    print(real[i])
#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

# class test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()