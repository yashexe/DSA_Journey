# Build Order: You are given a list of projects and a list of dependancies (which is
# a list of pairs of projects, where the 2nd project is dependant on the first project). All
# of a project's dependancies must be built before the project is. Find a build order
# that will allow the projects to be built. If there is no valid order, return an error.
# EX:
#   Input: projects: [a, b, c, d, e, f] dependancies: [(a,d), (f,b), (b,d), (f,a), (d,c)]
#   Output: [f, e, a, b, d, c]

import unittest
#-------------------------------------------------------------
class DirectedGraph:
    def __init__(self):
        self.adjacencyList = {}
    
    def __str__(self):
        for x in self.adjacencyList:
            print(f"{x}, {self.adjacencyList[x]}")

    def add_vertex(self, x):
        self.adjacencyList.setdefault(x, [])
        
    def add_edge(self, x, y):
        self.add_vertex(x)
        self.adjacencyList[x].append(y)

def buildOrder(projects, dependancies):
    if projects == []:
        raise Exception("No projects to be found!")
    elif dependancies is None:
        return projects
    elif not checkValidDependancies(dependancies):
        raise Exception("Dependances are invalid!")
    
    directed = DirectedGraph()
    
    for project in projects:
        directed.add_vertex(project)
    for dependancy in dependancies:
        directed.add_edge(dependancy[0],dependancy[1])

    removeDups(projects, directed.adjacencyList)

    return sort(directed.adjacencyList)
def sort(adj, complete = []):
    for key in adj:
        if key in complete:
            continue
        complete.append(key)

        for dependancy in adj[key]: 
            if dependancy not in complete:
                addDependancy(adj, dependancy, complete)
                break
            complete.pop()

            i = 0
            while i < len(complete) and complete[i] != dependancy: i+=1 
            
            if complete[i] == dependancy:
                complete.insert(i-1, key) if i-1 >= 0 else complete.insert(0, key)
                break
    return complete

def addDependancy(adj, key, complete):
    complete.append(key)
    if key in adj:
        for dependancy in adj[key]:
            if dependancy not in complete:
                addDependancy(adj, dependancy, complete)

def removeDups(projects, adj):
    remainingProjects = projects
    for key1 in remainingProjects:
        if adj[key1] == []:
            for key2 in remainingProjects:
                if adj[key2] != [] and key1 != key2 and key1 in adj[key2]:
                    del adj[key1]
                    remainingProjects = [project for project in remainingProjects if project != key1]
                    break

def checkValidDependancies(dependancies):
    for i in range(len(dependancies)):
        j = i + 1
        for j in range(len(dependancies)):
            if dependancies[i][0] == dependancies[j][1] and dependancies[i][1] == dependancies[j][0]: return False
    return True
#-------------------------------------------------------------
# Time: O(n^2) due to iterating over 'projects' with nested loop
# Space: O(V + E + projects) needs space proportional to verticies and edges
#-------------------------------------------------------------
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(buildOrder(["a","b","c","d","e","f"], [["a","d"],["f","b"],["b","d"],["f","a"],["d","c"]]),["f","b","a","d","c","e"])
        
    def test_singular_project(self):
        self.assertEqual(buildOrder(["a"], None),["a"])

    def test_error(self):
        with self.assertRaises(Exception):
            buildOrder(["a","b","c","d","e","f"], [["a","a"],["f","b"],["b","d"],["f","a"],["d","c"]])

if __name__ == "__main__":
    unittest.main()