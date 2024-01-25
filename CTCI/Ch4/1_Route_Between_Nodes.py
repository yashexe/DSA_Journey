# Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

import unittest
#-------------------------------------------------------------
class Node:
    def __init__(self, name, ):
        self.name = name
        self.children = []

    def add_children(self,child):
        self.children.append(child)

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self,name):
        self.nodes.append(Node(name))

def checkRoute(n1,n2, nodeDict = {}):

    if n2 in n1.children:
        return True
    
    elif n1 in nodeDict:

        return False
    
    for child in n1.children:
        nodeDict[child] = 1
        presence = checkRoute(child,n2,nodeDict)

        if presence:
            break

    return presence
g1 = Graph()
n1 = Node('Yash')
n2 = Node('Yash2')
n3 = Node('Yash3')
n0 = Node('No')
n1.add_children(n2)
n2.add_children(n3)

print(checkRoute(n1,n0))
#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

# class Test(unittest.TestCase):

# if __name__ == "__main__":
#     unittest.main()