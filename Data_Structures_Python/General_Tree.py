# General Tree: 0 or more children

class Tree_Node:
    def __init__(self,data = None):
        self.data = data
        self.children = []
    
def insert(root, parent_data, child_data):
    if root is None:
        root = Tree_Node(child_data)

    elif root.data == parent_data:
        root.children.append(Tree_Node(child_data))

    else:
        for i in range(len(root.children)):
            insert(root.children[i], parent_data, child_data)

def search(root, data):
    if root is None:
        return None
    elif root.data == data:
        return root
    else:
        for child in root.children:
            node = search(child, data)
            if node:
                return node
    return None

def level_order_traversal(root):
    if root is None:
        return 

    queue = [root]

    while queue:
        level = len(queue)
        
        for i in range(level):
            node = queue.pop(0)

            if node:
                print(node.data, end=' ')
            
                for child in node.children:
                    queue.append(child)
        print()
    
def delete(root, data):
    if root is None:
        return None
    
    elif root.data == data:
        if root.children:
            new_root = root.children.pop(0)

            new_root.children.extend(root.children)

            return new_root
        else:
            return None
    else:
        root.children = [delete(child,data) for child in root.children]

    return root
