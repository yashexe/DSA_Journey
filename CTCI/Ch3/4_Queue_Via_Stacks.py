# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

import unittest
#-------------------------------------------------------------
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        new_value = Node(value)

        new_value.next = self.top
        self.top = new_value

    def pop(self):
        if self.top is None:
            return None
        
        old_value = self.top.value
        self.top = self.top.next

        return old_value
    
    def peak(self):
        return self.top.value
    
class MyQueue:
    def __init__(self):
        pass
#-------------------------------------------------------------
# Time:
# Space:
#-------------------------------------------------------------
    
# class Test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()