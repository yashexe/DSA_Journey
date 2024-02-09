# Build Order: You are given a list of projects and a list of dependancies (which is
# a list of pairs of projects, where the 2nd project is dependant on the first project). All
# of a project's dependancies must be built before the project is. Find a build order
# that will allow the projects to be built. If there is no valid order, return an error.
# EX:
#   Input: projects: [a, b, c, d, e, f] dependancies: [(a,d), (f,b), (b,d), (f,a), (d,c)]
#   Output: [f, e, a, b, d, c]

import unittest
#-------------------------------------------------------------
class Graph:
    def __init__(self):
        self.adjacencyList = {}
    
    def __str__(self):
        for x in self.adjacencyList:
            print(f"x: {x}",
                  f", y: {self.adjacencyList[x]}" if self.adjacencyList[x] != [] else "")

    def add_vertex(self, x):
        if x not in self.adjacencyList:
            self.adjacencyList[x] = []
        else:
            raise Exception("This vertice already exists!")
        
    def add_edge(self, x, y):
        if x not in self.adjacencyList:
            self.add_vertex(x)
        if y not in self.adjacencyList:
            self.add_vertex(y)

        self.adjacencyList[x] = y

def buildOrder(projects, dependancies):
    if dependancies is None:
        return projects
    elif not checkValidDependancies(dependancies):
        raise Exception("Dependances are invalid!")

def checkValidDependancies(dependancies):
    for i in range(len(dependancies)):
        j = i + 1
        for j in range(len(dependancies)):
            if dependancies[i][0] == dependancies[j][1] and dependancies[i][1] == dependancies[j][0]:
                print(dependancies[i],dependancies[j])
                return False
    return True

def swap(projects, i, j):
    temp = projects[i]
    projects[i] = projects[j]
    projects[j] = temp


directed = Graph()

directed.add_edge("a","d")
directed.add_edge("f","b")
directed.add_edge("b","d")
directed.add_edge("f","a")
directed.add_edge("d","c")
directed.add_vertex("e")
directed.__str__()
#-------------------------------------------------------------
# Time:
# Space:
#-------------------------------------------------------------
# class Test(unittest.TestCase):
#     def setUp(self):
        
# if __name__ == "__main__":
#     unittest.main()