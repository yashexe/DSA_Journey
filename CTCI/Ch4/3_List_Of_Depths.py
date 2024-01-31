# List of Depths: Given a binary tree, design an algorithm which creates a linked
# list of all the nodes at each depth.

# e.g., if you have a tree with depth D, you'll have D linked lists

import unittest
from Binary_Search_Tree import Tree_Node, get_height, insert
#-------------------------------------------------------------
class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next
class SLL:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        curr = self.head
        result = []
        while curr:
            result.append(str(curr.data))
            curr = curr.next

        return "->".join(result)

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(data)

def listDepths(root):
    SLL_list = []
    
    getSLL(root, SLL_list)

    return SLL_list

def getSLL(root,SLL_list, currDepth = 0):
    if root is None:
        return

    elif len(SLL_list) == 0 or len(SLL_list) - 1 < currDepth:
        SLL_list.append(SLL())

    SLL_list[currDepth].add(root.data)

    currDepth += 1

    getSLL(root.left, SLL_list, currDepth)
    getSLL(root.right, SLL_list, currDepth)
#-------------------------------------------------------------
# Time: O(n) - determined by the height of the tree, if unbalanced, n
# Space: O(logn) - worst case tree is balanced, has 2^d - 1 nodes
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def setUp(self):
        # Create a sample binary search tree for testing
        # Modify this part based on your actual implementation
        self.root = Tree_Node(4)
        values = [ 2, 6, 1, 3, 5, 7]
        for value in values:
            self.root = insert(self.root, value)

    def test_list_depths_balanced_tree(self):
        # Test on a balanced tree
        result = listDepths(self.root)
        # Assuming you know the expected results for the test tree
        expected_result = [SLL(), SLL(), SLL(), SLL()]
        expected_result[0].add(4)
        expected_result[1].add(2)
        expected_result[1].add(6)
        expected_result[2].add(1)
        expected_result[2].add(3)
        expected_result[2].add(5)
        expected_result[2].add(7)

        # Check that the result matches the expected output
        self.assertEqual(result, expected_result)

    def test_list_depths_unbalanced_tree(self):
        # Test on an unbalanced tree
        values = [2, 3, 4, 5, 6, 7]
        unbalanced_root = Tree_Node(1)
        
        for value in values:
            unbalanced_root = insert(unbalanced_root, value)

        result = listDepths(unbalanced_root)
        # Assuming you know the expected results for the test tree
        expected_result = [SLL(), SLL(), SLL(), SLL(), SLL(), SLL(), SLL()]
        for i in range(7):
            expected_result[i].add(i + 1)

        # Check that the result matches the expected output
        self.assertEqual(result, expected_result)

    def test_list_depths_empty_tree(self):
        # Test on an empty tree
        empty_root = None
        result = listDepths(empty_root)
        # Expect an empty list since the tree is empty
        self.assertEqual(result, [])

    # Add more test cases if needed

if __name__ == "__main__":
    unittest.main()