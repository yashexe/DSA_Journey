# Binary Search Tree
# No duplicates, 0-2 children
class Tree_Node:
    def __init__(self,data,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def insert(node,data):
    if node is None:
        node = Tree_Node(data)
    else:
        insert_recursive(node,data)

def insert_recursive(node,data):
    if data < node.data:
        if node.left is None:
            node.left = Tree_Node(data)
        else:
            insert_recursive(node.left,data)
    elif data > node.data:
        if node.right is None:
            node.right = Tree_Node(data)
        else:
            insert_recursive(node.right,data)

def search(node,data):
    if node is None:
        return None
    elif data == node.data:
        return node
    elif data < node.data:
        return search(node.left,data)
    elif data > node.data:
        return search(node.right,data)


# BST = Tree_Node(10)

# insert(BST, 2)
# insert(BST, 3)
# insert(BST, 4)
# insert(BST, 12)
# insert(BST, 11)

# print(search(BST,11).data)