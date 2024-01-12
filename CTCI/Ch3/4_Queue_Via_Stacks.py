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

    def dequeue_1(self):
        if self.is_empty():
            return None
        
        if self.queue.top.next is None:
            return self.queue.pop()
        
        curr = self.queue.top

        while curr.next.next:
            curr = curr.next
        
        old_value = curr.next.value

        curr.next = None
        
        return old_value
    
    def dequeue_2(self):
        if self.is_empty():
            return None
        
        reverse_stack = Stack()

        while self.queue.top is not None:
            reverse_stack.push(self.queue.pop())

        old_value = reverse_stack.pop()

        while reverse_stack.top is not None:
            self.queue.push(reverse_stack.pop())

        
        return old_value
    
    def peak_1(self):
        if self.is_empty():
            return None
        
        curr = self.queue.top

        while curr.next:
            curr = curr.next
        
        return curr.value
    
    def peak_2(self):
        if self.is_empty():
            return None
        
        reverse_stack = Stack()

        while self.queue.top is not None:
            reverse_stack.push(self.queue.pop())

        peak_value = reverse_stack.peak()

        while reverse_stack.top is not None:
            self.queue.push(reverse_stack.pop())

        return peak_value
    def is_empty(self):
        return self.queue.top is None
#-------------------------------------------------------------
# Time: O(1) - enqueue, is_empty | O(2) - dequeue(1 and 2), peak(1 and 2)
# Space: O(1) - enqueue, is_empty, dequeue_1, peak_1 | O(n) - dequeue_2, peak_2
#-------------------------------------------------------------
    
class Test(unittest.TestCase):

    def test_enqueue(self):
        my_queue = MyQueue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(str(my_queue), "3->2->1")

    def test_dequeue_1(self):
        my_queue = MyQueue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.dequeue_1(), 1)
        self.assertEqual(str(my_queue), "3->2")

    def test_dequeue_2(self):
        my_queue = MyQueue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.dequeue_2(), 1)
        self.assertEqual(str(my_queue), "3->2")

    def test_peak_1(self):
        my_queue = MyQueue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.peak_1(), 1)

    def test_peak_2(self):
        my_queue = MyQueue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.peak_2(), 1)

    def test_is_empty(self):
        my_queue = MyQueue()
        self.assertTrue(my_queue.is_empty())
        my_queue.enqueue(1)
        self.assertFalse(my_queue.is_empty())
        my_queue.dequeue_1()
        self.assertTrue(my_queue.is_empty())

if __name__ == '__main__':
    unittest.main()