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
    
    def delete(self,key):
        if self.is_empty():
            return None
        elif self.head.value == key:
            return self.head.next
        
        temp = self.head

        while temp.next and temp.next.value != key:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

        return self.head

SLL = LinkedList()
SLL.add(1)
SLL.add(7)
SLL.add(3)
SLL.add(4)
print(SLL)