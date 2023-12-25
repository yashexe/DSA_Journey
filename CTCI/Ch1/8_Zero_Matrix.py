# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

import unittest
#-------------------------------------------------------------

def zero_matrix(matrix):
    zeros = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeros.append(f'{i}{j}')

    print(zeros)

    rows = set(s[0] for s in zeros)
    columns = set(s[1] for s in zeros)

    print(rows)
    print(columns)
    return matrix

zero_matrix([[1,0,3],[4,0,0],[0,8,9]])
#-------------------------------------------------------------
# Time:
# Space: 
#-------------------------------------------------------------

# class test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()