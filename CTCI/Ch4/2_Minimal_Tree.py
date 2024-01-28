# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height

import unittest
from Binary_Search_Tree import Tree_Node, insert, get_height
#-------------------------------------------------------------

def minimalTree(arr):
    if not arr:
        return
    
    mid = getMidpoint(arr)
    root = Tree_Node(arr.pop(mid))
    mid = getMidpoint(arr)
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
# Time: O(nlogn) - Array is split in half into 1 element segments
# Space: log(n) - balanced tree, O(1) for "mid"
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def test_minimalTree_empty(self):
        arr_empty = []
        self.assertIsNone(minimalTree(arr_empty))

    def test_minimalTree_single(self):
        arr_single = [5]
        root_single = minimalTree(arr_single)
        self.assertEqual(get_height(root_single), 1)

    def test_minimalTree_odd(self):
        arr_odd = [1, 2, 3, 4, 5]
        root_odd = minimalTree(arr_odd)
        self.assertTrue(0 <= abs(get_height(root_odd.left) - get_height(root_odd.right)) <= 1)

    def test_minimalTree_even(self):
        arr_even = [1, 2, 3, 4]
        root_even = minimalTree(arr_even)
        self.assertTrue(0 <= abs(get_height(root_even.left) - get_height(root_even.right)) <= 1)

if __name__ == "__main__":
    unittest.main()