# BST Sequences: A BST was created by traversing through an array from left to right
# and inserting each element. Given a BST with distinct elements, print all possible
# arrays that couldve lead to this tree.
# EXAMPLE: 2
#         1 3
# Output: {2, 1, 3}, {2, 3, 1}
import unittest
from Binary_Search_Tree import Tree_Node, insert_multiple,insert
#-------------------------------------------------------------
def BST_Sequences(root):
    arrSize = 2 ** getHeight(root) - 1

    arr = toArr(root, [0 for i in range(arrSize)])

    return checkSequences(arr, [arr], arrSize)

def getHeight(root, height = 0):
    if root is None: return height

    l = getHeight(root.left, height)
    r = getHeight(root.right, height)

    return max(l, r) + 1

def toArr(root, arr, i = 0):
    if root is None: return arr

    arr[i] = root.data

    arr = toArr(root.left, arr, 2*i + 1)
    arr = toArr(root.right, arr, 2*i + 2)

    return arr

def checkSequences(arr, sequences, size, i = 0):
    if i > size - 1 or arr[i] == 0:
        return
    print(i, arr[i])
    left = checkChildren(arr, 2*i+1, size)
    right = checkChildren(arr, 2*i+2, size)

    if left != None: sequences.append(left)

    if right != None: sequences.append(right)

    checkSequences(arr, sequences, size, 2*i+1)
    checkSequences(arr, sequences, size, 2*i+2)

    return sequences 

def checkChildren(arr, i, size):
    if i >= (size - 1)/2: return None
    
    if arr[2*i + 1] != 0 and arr[2*i + 2] != 0:
        tempArr = arr
        tempArr[2*i + 1], tempArr[2*i + 2] = tempArr[2*i + 2], tempArr[2*i + 1]
        return tempArr
    else: return None

#-------------------------------------------------------------
# Time: O(n), both time and space depend on the number of nodes in root tree
# Space: O(n)
#-------------------------------------------------------------
BST = Tree_Node(5)
insert_multiple(BST, [3, 7, 2, 4, 6, 8])
sequences = BST_Sequences(BST)

for sequence in sequences: print(sequence)
# class Test(unittest.TestCase):
#     pass
# if __name__ == "__main__":
#     unittest.main()