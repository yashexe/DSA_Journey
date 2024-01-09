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
        if self.is_empty():
            print('No Sets')
        for i in range(len(self.set)):
            print(f'Stack {i}:', self.set[i].__str__())
            
    def push(self, value):
        if self.is_empty() or self.set[self.latest].num == self.threshold:
            new_stack = SetOfStacks_Stack()
            new_stack.push(value)

            if self.is_empty():
                self.latest = 0
            else:
                self.latest += 1

            self.set.append(None)

            self.set[self.latest] = new_stack

        else:
            self.set[self.latest].push(value)

    def pop(self):
        if self.is_empty():
            return None
        
        if self.set[self.latest].num == 1:

            old_value = self.set[self.latest].pop()

            self.set.pop()
            self.latest = self.latest - 1 if self.latest > 0 else None
                
            return old_value
        
        return self.set[self.latest].pop()
    
    def is_empty(self):
        return not self.set
#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------
# FOLLOW UP: Implement a function popAt(index) which performs a pop operation on a specific sub-stack
#-------------------------------------------------------------
    def popAt(self,index):
        pass

SS = SetOfStacks(3)

SS.push(1)
SS.push(2)
SS.push(3)
SS.push(2)
SS.push(2)

SS.pop()
SS.__str__()

#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

# class Test(unittest.TestCase):
        
# if __name__ == '__main__':
#     unittest.main()
