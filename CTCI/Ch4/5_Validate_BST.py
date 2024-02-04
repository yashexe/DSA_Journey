# Validate BST: Implement a function to check if a Binary Tree is
# a BInary Search Tree.

# A Binary Tree node has 0-2 children
# A BST 
import unittest
from Binary_Search_Tree import Tree_Node,insert
#-------------------------------------------------------------
def validateBST(root):
    if not root: 
        return True
    if root.left and root.left.data > root.data or root.right and root.right.data < root.data:
        return False
    if root.left is None and root.right is None:
        return True
    
    isBST = validateBST(root.left)
    if isBST:
        isBST = validateBST(root.right)

    return isBST
#-------------------------------------------------------------
# Time: O(n) - must run through all nodes of BST at worst case(Balanced)
# Space: O(h) - Recursive call stack stores at most the height of BST
#-------------------------------------------------------------
class Test(unittest.TestCase):
    def setUp(self):

        self.empty_bst = Tree_Node(None)

        self.single_node_bst = Tree_Node(10)

        self.binary_tree = Tree_Node(5)
        self.binary_tree.left = Tree_Node(2)
        self.binary_tree.right = Tree_Node(9)
        self.binary_tree.right.right = Tree_Node(10)
        self.binary_tree.right.left = Tree_Node(8)
        self.binary_tree.left.right = Tree_Node(4)
        self.binary_tree.left.left = Tree_Node(8)

        self.binary_search_tree = Tree_Node(5)
        for element in [3, 7, 10, 6, 2, 4]:
            insert(self.binary_search_tree, element)
        
    def test_empty_tree(self):
        self.assertEqual(validateBST(self.empty_bst), True)

    def test_root(self):
        self.assertEqual(validateBST(self.single_node_bst), True)

    def test_binary_tree(self):
        self.assertEqual(validateBST(self.binary_tree), False)

    def test_binary_search_tree(self):
        self.assertEqual(validateBST(self.binary_search_tree), True)
        
if __name__ == "__main__":
    unittest.main()