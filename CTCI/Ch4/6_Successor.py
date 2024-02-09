# Successor: Write an algorithm to find the "next" node(i.e., in-order successor) of a given node in a BST.
# You may assume each node has a link to it's parent.
import unittest
from Binary_Search_Tree import Tree_Node,insert
#-------------------------------------------------------------
def findSuccessor(node):
    if node.up is None and node.left is None and node.right is None:
        return None

    curr = node
    while curr.up is not None:
        curr = curr.up

    arr = []
    toInOrderArray(curr, arr)

    for i in range(len(arr)):
        return arr[i + 1] if arr[i] == node and i < len(arr) - 1 else None

def toInOrderArray(root, arr):
    if root is None: return

    toInOrderArray(root.left, arr)

    arr.append(root)

    toInOrderArray(root.right, arr)

#-------------------------------------------------------------
# Time: O(n) iterates through all nodes
# Space: O(n) - Stores all nodes in tree
#-------------------------------------------------------------
