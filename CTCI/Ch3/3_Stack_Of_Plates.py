# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might
# topple. Therefore, in real life, we would likely start a new stack when the previous stack
# exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks
# should be composed of several stacks and should create a new stack once the previous one exceeds
# capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).

import unittest
#-------------------------------------------------------------
class SetOfStacks_Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class SetOfStacks:
    def __init__(self):

        self.set = []
        
#-------------------------------------------------------------
# Time: O(1) - for all operations
# Space: O(n) - n elements in stack
#-------------------------------------------------------------
# FOLLOW UP: Implement a function popAt(index) which performs a pop operation on a specific sub-stack
#-------------------------------------------------------------


    def popAt(self,index):

        return None

#-------------------------------------------------------------
# Time: O()
# Space: O()
#-------------------------------------------------------------

# class Test(unittest.TestCase):
        
# if __name__ == '__main__':
#     unittest.main()
