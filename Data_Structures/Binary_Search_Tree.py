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

def delete(node,data):
    if node is None:
        return None
    
    elif data < node.data:
        node.left = delete(node.left,data)
    elif data > node.data:
        node.right = delete(node.right,data)

    elif data == node.data:
        if node.right is None:
            return node.left
        elif node.left is None:
            return node.right

        node.data = minimum(node.right)

        node.right = delete(node.right, node.data)

    return node

def minimum(node):
    while node.left:
        node = node.left
    return node.data

def maximum(node):
    while node.right:
        node = node.right
    return node.data

def pre_order_traverse(node):
    if node is not None:
        print(node.data, end=' ')
        pre_order_traverse(node.left)
        pre_order_traverse(node.right)

def in_order_traverse(node):
    if node is not None:
        in_order_traverse(node.left)
        print(node.data, end=' ')
        in_order_traverse(node.right)

def post_order_traverse(node):
    if node is not None:
        post_order_traverse(node.left)
        post_order_traverse(node.right)
        print(node.data, end=' ')

