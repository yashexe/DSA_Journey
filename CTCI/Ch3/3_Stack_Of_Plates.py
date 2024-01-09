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

class SetOfStacks_Stack:
    def __init__(self):
        self.top = None
        self.num = 0

    def __str__(self):
        curr = self.top
        result = []
        
        while curr:
            result.append(str(curr.value))
            curr = curr.next
        
        return '->'.join(result)
    
    def push(self,value):
        new_node = SetOfStacks_Node(value)

        new_node.next = self.top
        self.top = new_node

        self.num += 1

    def pop(self):
        if self.top is None:
            return None
        
        old_node = self.top.value

        self.top = self.top.next

        self.num -= 1
        return old_node

class SetOfStacks:
    def __init__(self,threshold = 10):
        self.threshold = threshold
        self.set = []
        self.latest = None

    def __str__(self):
        if not self.set:
            print('No Sets')
        for i in range(len(self.set)):
            print(f'Stack {i}:', self.set[i].__str__())
            
    def push(self, value):
        if not self.set or self.set[self.latest].num == self.threshold:
            new_stack = SetOfStacks_Stack()
            new_stack.push(value)

            self.latest = self.latest + 1 if self.set else 0

            self.set.append(None)

            self.set[self.latest] = new_stack

        else:
            self.set[self.latest].push(value)

    def pop(self):
        if not self.set:
            return None
        
        if self.set[self.latest].num <= 1:

            old_value = self.set[self.latest].pop()

            self.set.pop()
            self.latest = self.latest - 1 if self.latest > 0 else None
                
            return old_value
        
        return self.set[self.latest].pop()
#-------------------------------------------------------------
# Time: O(1)
# Space: O(n+m) - n is the # of stacks in the set, and m is the total # of elements in all stacks
#-------------------------------------------------------------
# FOLLOW UP: Implement a function popAt(index) which performs a pop operation on a specific sub-stack
#-------------------------------------------------------------
    def popAt(self,index):
        if self.latest is None or index > self.latest or index < 0:
            raise IndexError('Invalid Index value.')
        
        elif self.set[index].num == 1:
            old_value = self.set[index].pop()

            if index == self.latest:
                self.latest = self.latest - 1 if self.latest > 0 else None
                self.set.pop()

            return old_value

        return self.set[index].pop()

#-------------------------------------------------------------
# Time: O(1)
# Space: O(1)
#-------------------------------------------------------------

class Test(unittest.TestCase):

    def test_push_pop(self):
        set_of_stacks = SetOfStacks(threshold=3)
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for value in values:
            set_of_stacks.push(value)

        popped_values = []
        while True:
            value = set_of_stacks.pop()
            if value is None:
                break
            popped_values.append(value)

        self.assertEqual(popped_values, values[::-1])

    def test_pop_at(self):
        set_of_stacks = SetOfStacks(threshold=3)
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for value in values:
            set_of_stacks.push(value)

        popped_value = set_of_stacks.popAt(1)
        self.assertEqual(popped_value, 6)

        popped_value = set_of_stacks.popAt(0)
        self.assertEqual(popped_value, 3)

        popped_value = set_of_stacks.popAt(2)
        self.assertEqual(popped_value, 9)

        with self.assertRaises(IndexError):
            set_of_stacks.popAt(3)

    def test_push_after_pop_at(self):
        set_of_stacks = SetOfStacks(threshold=2)
        values = [1, 2, 3, 4, 5, 6]

        for value in values:
            set_of_stacks.push(value)

        popped_value = set_of_stacks.popAt(1)
        self.assertEqual(popped_value, 4)

        set_of_stacks.push(10)

        popped_value = set_of_stacks.popAt(0)
        self.assertEqual(popped_value, 2)

        popped_values = []
        while True:
            value = set_of_stacks.pop()
            if value is None:
                break
            popped_values.append(value)

        self.assertEqual(popped_values, [10, 6, 5, 3, 1])

if __name__ == '__main__':
    unittest.main()
