# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height

import unittest
from Binary_Search_Tree import Tree_Node
#-------------------------------------------------------------

def minimalTree(arr):
    insert(arr)

def insert(arr, root = None):
    if root is None:
        root = Tree_Node(arr.pop(getMidpoint(arr)))

    elif arr == []:
        return
    elif root and arr:
        pass
    
def getMidpoint(arr):
    return (len(arr) - 1) // 2

def travserse(data, root):
    if not root.left and not root.right:
        return root
    if root.left and root.left > data:
        root = travserse(data, root.left)
    if root.left and root.right < data:
        root = travserse(data, root.right)
#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

# class Test(unittest.TestCase):
#     def setUp(self):

# if __name__ == "__main__":
#     unittest.main()