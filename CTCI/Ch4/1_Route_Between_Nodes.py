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
    if n1 == n2:
        return True
    
    if n2 in n1.children:
        return True
    
    elif n1 in nodeDict:
        return False
    
    for child in n1.children:
        presence = checkRoute(child,n2,nodeDict)
        nodeDict[child] = 1

        if presence:
            return True

    return False

#-------------------------------------------------------------
# Time: O(V+E) - Worst Case, every vertex and edge visited
# Space: O(V) - Worst Case, graph is a straight line, need to visit all vertices
# with recursive call stack
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def setUp(self):
        self.node1 = Node("A")
        self.node2 = Node("B")
        self.node3 = Node("C")
        self.node4 = Node("D")

        self.node1.add_children(self.node2)
        self.node2.add_children(self.node3)
        self.node3.add_children(self.node4)

    def test_route_exists(self):
        result = checkRoute(self.node1, self.node4)
        self.assertTrue(result)

    def test_route_does_not_exist(self):
        result = checkRoute(self.node4, self.node1)
        self.assertFalse(result)

    def test_same_node(self):
        result = checkRoute(self.node1, self.node1)
        self.assertTrue(result)

    def test_node_not_in_graph(self):
        new_node = Node("E")
        result = checkRoute(self.node1, new_node)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()