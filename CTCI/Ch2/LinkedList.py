#Singly Linked Lists

# [] -> [] -> [] ->


class Node:
    def __init__(self, value,next_node = None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        str_ll = []
        curr = self.head

        while curr:
            str_ll.append(str(curr.value))
            curr = curr.next

        return ' -> '.join(str_ll)

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
            return curr.next
    
    def group_add(self,values):
        for value in values:
            self.add(value)
    
    def to_list(self):
        if not self.head:
            return []
        
        curr = self.head
        arr = []

        while curr:
            arr.append(curr.value)
            curr = curr.next

        return arr
    
    def length(self):
        length = 0
        curr = self.head

        while curr:
            length += 1
            curr = curr.next

        return length
    
    def delete(self,key):
        if self.is_empty():
            return None
        
        if self.head.value == key:
            self.head = self.head.next
            return self.head.next
        
        temp = self.head

        while temp.next and temp.next.value != key:
            temp = temp.next
            
        if temp.next:
            temp.next = temp.next.next

        return self.head