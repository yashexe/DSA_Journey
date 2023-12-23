# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

import unittest
#-------------------------------------------------------------

def zero_matrix(matrix):
    zero_dict = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_dict[f'{i},{j}'] = 1
    
    
    return matrix

#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

# class test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()