# First Common Ancestor: Design an algorithm and write code to find the first
# common ancestor of two nodes in a binary tree. Avoid storing additional nodes
# in a data structure.
# note: This is not necessarily a BST.
import unittest
from Binary_Search_Tree import Tree_Node
#-------------------------------------------------------------

def firstCommonAncestor(BT, n1, n2):
    if not BT: return None

    h1 = getHeight(BT, n1)
    h2 = getHeight(BT, n2)

    if h1 is None or h2 is None:
        return None

    while n1 != n2 or h1 != h2:
        if h1 > h2:
            n1 = search(BT, n1)
            h1 -=1 
        elif h2 > h1:
            n2 = search(BT, n2)
            h2 -=1 
        else:
            n1 = search(BT, n1)
            n2 = search(BT, n2)

    return n1

def search(treeNode, node):
    if treeNode is None:
        return None
    elif treeNode == node or treeNode.left == node or treeNode.right == node:
        return treeNode

    left = search(treeNode.left, node)
    
    if left:
        return left
    return search(treeNode.right, node)


def getHeight(treeNode, node, height=0):
    if treeNode is None:
        return None
    elif treeNode == node:
        return height
    
    left = getHeight(treeNode.left, node, height + 1)

    if left:
        return left
    return getHeight(treeNode.right, node, height + 1)
#-------------------------------------------------------------
# Time: O(n) - n is the height of the tree, exact number depends on ancestor
# Space: O(1) - No additional space
#-------------------------------------------------------------
class Test(unittest.TestCase):
    def test_first_common_ancestor_same_node(self):
        BT = Tree_Node(4)
        self.assertEqual(firstCommonAncestor(BT, BT, BT), BT)

    def test_first_common_ancestor_simple_tree(self):
        BT = Tree_Node(4)
        BT.left = Tree_Node(5)
        BT.left.left = Tree_Node(6)
        BT.left.right = Tree_Node(7)
        self.assertEqual(firstCommonAncestor(BT, BT.left.left, BT.left.right), BT.left)

    def test_first_common_ancestor_nodes_at_different_depths(self):
        BT = Tree_Node(4)
        BT.left = Tree_Node(5)
        BT.left.left = Tree_Node(6)
        BT.left.right = Tree_Node(7)
        BT.left.right.left = Tree_Node(8)
        self.assertEqual(firstCommonAncestor(BT, BT.left.left, BT.left.right.left), BT.left)

    def test_first_common_ancestor_nodes_far_apart(self):
        BT = Tree_Node(4)
        BT.left = Tree_Node(5)
        BT.left.left = Tree_Node(6)
        BT.right = Tree_Node(7)
        BT.right.right = Tree_Node(8)
        self.assertEqual(firstCommonAncestor(BT, BT.left.left, BT.right.right), BT)

    def test_first_common_ancestor_nodes_not_in_tree(self):
        BT = Tree_Node(4)
        BT.left = Tree_Node(5)
        BT.right = Tree_Node(6)
        BT.left.left = Tree_Node(7)
        BT.right.right = Tree_Node(8)
        self.assertIsNone(firstCommonAncestor(BT, Tree_Node(9), Tree_Node(10)), None)

if __name__ == "__main__":
    unittest.main()