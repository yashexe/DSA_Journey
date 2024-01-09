# Stack Min: How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop and min should all
# operate in O(1) time.

import unittest

#-------------------------------------------------------------
#All functions need O(1) time complexity
#set/dict not possible as they are not ordered
#min implemented with recursion not possible as it'll be >O(1)
#Another Stack defined in __init__? Cant be ordered though, with O(1) at least..

class Stack_Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)
    
class Stack:
    def __init__(self):
        self.top = None
        self.curr_min = None
        self.ordered_mins = []

    def push(self, value):
        if not self.curr_min or value <= self.curr_min:
            self.curr_min = value
            self.ordered_mins.append(value)

        new_node = Stack_Node(value)
        new_node.next = self.top

        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        
        old_value = self.top.value

        if old_value == self.ordered_mins[-1]:
            self.ordered_mins.pop()
            self.curr_min = self.ordered_mins[-1] if self.ordered_mins else None

        self.top = self.top.next

        return old_value
    
    def min(self):
        if self.top is None:
            return None

        return self.curr_min

#-------------------------------------------------------------
# Time: O(1) - for all operations
# Space: O(n) - n elements in stack
#-------------------------------------------------------------

# class Test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()
