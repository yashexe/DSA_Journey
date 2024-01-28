# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height

import unittest
from Binary_Search_Tree import Tree_Node
#-------------------------------------------------------------

def minimalTree(arr):
    if not arr:
        return
    root = Tree_Node(arr.pop((len(arr)) - 1) // 2)
    
    minimalTreeRecursive(arr,root)

def minimalTreeRecursive(arr, node = None):
    if not arr:
        return
#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

# class Test(unittest.TestCase):
#     def setUp(self):

# if __name__ == "__main__":
#     unittest.main()