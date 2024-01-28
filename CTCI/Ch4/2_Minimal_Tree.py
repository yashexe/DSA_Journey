# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height

import unittest
from Binary_Search_Tree import Tree_Node, insert,in_order_traverse, pre_order_traverse, post_order_traverse
#-------------------------------------------------------------

def minimalTree(arr):
    if not arr:
        return
    
    mid = getMidpoint(arr)
    root = Tree_Node(arr.pop(mid))

    minimalTreeRecursive(arr[:mid],root)
    minimalTreeRecursive(arr[mid:],root)

    return root

def minimalTreeRecursive(arr, root = None):
    if not arr:
        return

    mid = getMidpoint(arr)

    insert(root,arr[mid])

    if mid == 0:
        return
    
    minimalTreeRecursive(arr[mid:], root)
    minimalTreeRecursive(arr[:mid], root)

def getMidpoint(arr):
    return len(arr) // 2

#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

# class Test(unittest.TestCase):
#     def setUp(self):

# if __name__ == "__main__":
#     unittest.main()