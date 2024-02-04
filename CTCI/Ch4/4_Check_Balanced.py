# Check Balanced: Implement a function to check if a binary tree is balanced. For the
# purposes of the question, a balanced tree is defined to be a tree such that the
# height of the two subtrees of any node never differ by more than 1.
import unittest
from Binary_Search_Tree import Tree_Node,insert
#-------------------------------------------------------------
def checkBalanced(root):
    if bool(root.left) != bool(root.right):
        return False
    elif not bool(root.left) and not bool(root.right):
        return True

    isBalanced = checkBalanced(root.left)
    if isBalanced:
        isBalanced = checkBalanced(root.right)

    return isBalanced
#-------------------------------------------------------------
# Time: O(n) - must run through all nodes of BST at worst case(Balanced)
# Space: O(h) - Recursive call stack stores at most the height of BST
#-------------------------------------------------------------
class Test(unittest.TestCase):
    def setUp(self):

        self.empty_bst = Tree_Node(None)

        self.single_node_bst = Tree_Node(10)

        self.balanced_bst = Tree_Node(5)
        for element in [3, 7, 10, 6, 2, 4]:
            insert(self.balanced_bst, element)

        self.not_balanced_bst = Tree_Node(5)
        for element in [3, 7, 10]:
            insert(self.not_balanced_bst, element)

    def test_empty(self):
        self.assertEqual(checkBalanced(self.empty_bst), True)

    def test_root(self):
        self.assertEqual(checkBalanced(self.single_node_bst), True)

    def test_not_balanced(self):
        self.assertEqual(checkBalanced(self.not_balanced_bst), False)

    def test_balanced(self):
        self.assertEqual(checkBalanced(self.balanced_bst), True)

if __name__ == "__main__":
    unittest.main()