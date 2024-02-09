# Build Order: You are given a list of projects and a list of dependancies (which is
# a list of pairs of projects, where the 2nd project is dependant on the first project). All
# of a project's dependancies must be built before the project is. Find a build order
# that will allow the projects to be built. If there is no valid order, return an error.
# EX:
#   Input: projects: [a, b, c, d, e, f] dependancies: [(a,d), (f,b), (b,d), (f,a), (d,c)]
#   Output: [f, e, a, b, d, c]

import unittest
from Binary_Search_Tree import Tree_Node,insert
#-------------------------------------------------------------
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
#-------------------------------------------------------------
# Time:
# Space:
#-------------------------------------------------------------
# class Test(unittest.TestCase):
#     def setUp(self):
        
# if __name__ == "__main__":
#     unittest.main()