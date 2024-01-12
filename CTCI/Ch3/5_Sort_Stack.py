# Sort Stack: Write a program to sort a stack such that the smallest items are on 
# the top. You can use an additional stack, but you may not copy the elements into
# any other data structure (such as an array). The stack supports the following
# operations. push, pop, peek, and is_empty.

import unittest
#-------------------------------------------------------------
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        curr = self.top
        stack_list = []
        while curr:
            stack_list.append(str(curr.value))
            curr = curr.next
        return '->'.join(stack_list)
    
    def push(self,value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None
        
        old_value = self.top.value
        self.top = self.top.next

        return old_value
    
    def peek(self):
        return self.top.value
    
    def is_empty(self):
        return self.top is None

def sort_stack(s1):
    if s1.is_empty() or s1.top.next is None:
        return

    unordered = False
    curr = s1.top

    while True:
        if curr.value > curr.next.value:
            print(s1.__str__())
            temp = curr.value
            curr.value = curr.next.value
            curr.next.value = temp

            unordered = True

        if not unordered and curr.next.next is None:
            print(s1.__str__())
            return
        elif unordered and curr.next.next is None:
            unordered = False
            curr = s1.top
        else:
            curr = curr.next

#-------------------------------------------------------------
# Time: O(n^2)
# Space: O(1)
#-------------------------------------------------------------
    
# class Test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()