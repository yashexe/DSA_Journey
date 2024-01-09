# Three in One: Describe how you can use a single array to implement three stacks

import unittest
#-------------------------------------------------------------

# Each stack is allocated a specific segment in the array.
# The class provides methods to push, pop, check if empty, and peek for each stack.

class Three_Stack:
    def __init__(self, size = 10):
        self.items = [None] * ((size + 1)*3)
        self.size = size
        self.top1 = 0
        self.top2 = size + 1
        self.top3 = 2*(size + 1)

    def __str__(self, num):
        if num == 1:
            print('Stack 1: ')
            for i in range(self.size + 1, 0, -1):
                print(self.items[i]) if self.items[i] is not None else None

        elif num == 2:
            print('Stack 2: ')
            for i in range(2*self.size + 1, self.size + 1, -1):
                print(self.items[i]) if self.items[i] is not None else None

        elif num == 3:
            print('Stack 3: ')
            for i in range(len(self.items) - 1, 2*self.size + 2, -1):
                print(self.items[i]) if self.items[i] is not None else None

        else:
            return IndexError('Invalid num, must be 1, 2 or 3')
        
    def push(self, num, value):
        if num == 1 and self.top1 != self.size:
            self.items[self.top1 + 1] = value
            self.top1 += 1
        elif num == 2 and self.top2 != (2*self.size + 1):
            self.items[self.top2 + 1] = value
            self.top2 += 1
        elif num == 3:                 # no restriction on size, since it's last
            self.items[self.top3 + 1] = value
            self.top3 += 1
        elif num < 1 or num >3:
            return IndexError('Invalid num, must be 1, 2 or 3')
        else:
            return None
        
    def is_empty(self, num):
        if num == 1:
            return self.items[self.top1] is None
        elif num == 2:
            return self.items[self.top2] is None
        elif num == 3:
            return self.items[self.top3] is None
        else:
            return IndexError('Invalid num, must be 1, 2 or 3')
        
    def pop(self,num):
        if num == 1 and not self.is_empty(1):
            old_value = self.items[self.top1]

            self.items[self.top1] = None
            self.top1 -= 1

            return old_value
        
        elif num == 2 and not self.is_empty(2):
            old_value = self.items[self.top2]

            self.items[self.top2] = None
            self.top2 -= 1

            return old_value
        
        elif num == 3 and not self.is_empty(3):
            old_value = self.items[self.top3]

            self.items[self.top3] = None
            self.top3 -= 1

            return old_value
        elif num < 1 or num > 3:
            return IndexError('Invalid num, must be 1, 2 or 3')
        else: return None

    def peek(self, num):
        if num == 1:
            return self.items[self.top1]
        elif num == 2:
            return self.items[self.top2]
        elif num == 3:
            return self.items[self.top3]
        else:
            return IndexError('Invalid num, must be 1, 2 or 3')
#-------------------------------------------------------------
# Time: O(1)
# Space: O(1)
# For __str__:
# Time: O(n)
# Space: O(1)
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def setUp(self):
        self.three_stack = Three_Stack()

    def test_push_pop_stack1(self):
        self.three_stack.push(1, 10)
        self.assertEqual(self.three_stack.pop(1), 10)

    def test_push_pop_stack2(self):
        self.three_stack.push(2, 20)
        self.assertEqual(self.three_stack.pop(2), 20)

    def test_push_pop_stack3(self):
        self.three_stack.push(3, 30)
        self.assertEqual(self.three_stack.pop(3), 30)

    def test_peek_empty_stack(self):
        self.assertIsNone(self.three_stack.peek(1))
        self.assertIsNone(self.three_stack.peek(2))
        self.assertIsNone(self.three_stack.peek(3))

    def test_push_pop_multiple_elements(self):
        self.three_stack.push(1, 10)
        self.three_stack.push(2, 20)
        self.three_stack.push(3, 30)
        
        self.assertEqual(self.three_stack.pop(1), 10)
        self.assertEqual(self.three_stack.pop(2), 20)
        self.assertEqual(self.three_stack.pop(3), 30)

    def test_push_to_full_stack(self):
        for i in range(11):
            self.three_stack.push(1, i)
        self.assertIsNone(self.three_stack.push(1, 99))

    def test_pop_empty_stack(self):
        self.assertIsNone(self.three_stack.pop(1))
        self.assertIsNone(self.three_stack.pop(2))
        self.assertIsNone(self.three_stack.pop(3))
if __name__ == '__main__':
    unittest.main()
