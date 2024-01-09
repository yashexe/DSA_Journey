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
        self.ordered_mins = []

    def push(self, value):
        if not self.ordered_mins or value <= self.ordered_mins[-1]:
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

        self.top = self.top.next

        return old_value
    
    def min(self):
        if self.top is None:
            return None

        return self.ordered_mins[-1]
#-------------------------------------------------------------
# Time: O(1) - for all operations
# Space: O(n) - n elements in stack
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        stack.push(3)
        stack.push(5)
        stack.push(2)

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), None) 

    def test_min(self):
        stack = Stack()
        stack.push(3)
        stack.push(5)
        stack.push(2)

        self.assertEqual(stack.min(), 2)

        stack.pop()

        self.assertEqual(stack.min(), 3)

    def test_empty_stack(self):
        stack = Stack()

        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.min(), None)

    def test_min_with_duplicates(self):
        stack = Stack()
        stack.push(3)
        stack.push(5)
        stack.push(2)
        stack.push(2)

        self.assertEqual(stack.min(), 2)

        stack.pop()

        self.assertEqual(stack.min(), 2)

    def test_min_empty_stack(self):
        stack = Stack()

        self.assertEqual(stack.min(), None)

    def test_min_after_popping_all_elements(self):
        stack = Stack()
        stack.push(3)
        stack.push(5)
        stack.push(2)

        stack.pop()
        stack.pop()
        stack.pop()

        self.assertEqual(stack.min(), None)
        
if __name__ == '__main__':
    unittest.main()
