# Stack
# LIFO: Last in, First out

# 5(self.top) -> 3 -> 1 -> None

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
        if self.is_empty():
            return None
        
        old_value = self.top.value
        self.top = self.top.next

        return old_value
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self.top.value
    
    def is_empty(self):
        return self.top is None