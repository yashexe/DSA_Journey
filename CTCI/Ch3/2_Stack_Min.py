# Stack Min: How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop and min should all
# operate in O(1) time.

import unittest

#-------------------------------------------------------------
class Stack_Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):

        new_node = Stack_Node(value)
        new_node.next = self.top

        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        
        old_value = self.top.value
        self.top = self.top.next
        
        return old_value
    
    def min(self):
        if self.top is None:
            return None

        return

    

#-------------------------------------------------------------
# Time:
# Space:
#-------------------------------------------------------------

# class Test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()
