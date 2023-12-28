#Singly Linked Lists

# [] -> [] -> [] ->


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def add(self,value):
        if self.is_empty():
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(value)
    
    def delete(self,key):
        temp = self.head

        if temp.value == key:
            return self.head.next


