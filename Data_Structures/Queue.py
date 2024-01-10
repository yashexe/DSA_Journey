# Queues
# IN -> 1-> 2-> 3-> OUT

class Queue_Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)
    
class Queue:
    def __init__(self):
        self.rear = None #FI
        self.front = None #FO

    def __str__(self):
        curr = self.front

        queue_list = []
        while curr:
            queue_list.append(str(curr.value))
            curr = curr.next

        return '->'.join(reversed(queue_list))

    def enqueue(self,value):
        new_value = Queue_Node(value)

        if self.is_empty():
            self.rear = self.front = new_value
        else:
           self.rear.next = new_value
           self.rear = new_value

    def dequeue(self):
        if self.is_empty():
            return None
        
        old_value = self.front.value
        self.front = self.front.next
        return old_value

    def end(self):
        return self.front.value
    
    def start(self):
        return self.rear.value

    def is_empty(self):
        return self.front is None