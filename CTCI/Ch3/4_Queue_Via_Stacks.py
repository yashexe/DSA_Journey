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

    def __str__(self):
        curr = self.top
        stack_list = []
        while curr:
            stack_list.append(str(curr.value))
            curr = curr.next
        return '->'.join(stack_list)
    
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
    
    def is_empty(self):
        return self.top is None
    
class MyQueue:
    def __init__(self):
        self.queue = Stack()

    def __str__(self):
        return self.queue.__str__()
    
    def enqueue(self, value):
        self.queue.push(value)

    def dequeue(self):
        if self.is_empty():
            return None

        curr = self.queue.top

        while curr.next.next:
            curr = curr.next
        
        old_value = curr.next.value

        curr.next = None
        
        return old_value

    def peak(self):
        if self.is_empty():
            return None

        curr = self.queue.top

        while curr.next:
            curr = curr.next
        
        return curr.value

    def is_empty(self):
        return self.queue.top is None
Q = MyQueue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)

print(Q.__str__())
print(Q.peak())

Q.dequeue()

print(Q.__str__())
print(Q.peak())

Q.enqueue(3)

print(Q.__str__())
#-------------------------------------------------------------
# Time:
# Space:
#-------------------------------------------------------------
    
# class Test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()