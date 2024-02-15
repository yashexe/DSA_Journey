# BST Sequences: A BST was created by traversing through an array from left to right
# and inserting each element. Given a BST with distinct elements, print all possible
# arrays that couldve lead to this tree.
# EXAMPLE: 2
#         1 3
# Output: {2, 1, 3}, {2, 3, 1}
import unittest
from Binary_Search_Tree import Tree_Node, insert_multiple
#-------------------------------------------------------------
def BST_Sequences(root):
    arrSize = 2 ** getHeight(root) - 1

    arr = toArr(root, [0 for i in range(arrSize)])

    return arr

def toArr(root, arr, i = 0):
    if root is None: return arr

    arr[i] = root.data

    arr = toArr(root.left, arr, 2*i + 1)
    arr = toArr(root.right, arr, 2*i + 2)

    return arr

def getHeight(root, height = 0):
    if root is None: return height
    
    l = getHeight(root.left, height)
    r = getHeight(root.left, height)

    return max(l,r) + 1
#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------
BST = Tree_Node(5)
insert_multiple(BST, [3, 7, 2, 4, 6, 8])

print(BST_Sequences(BST))
# class Test(unittest.TestCase):
#     pass
# if __name__ == "__main__":
#     unittest.main()