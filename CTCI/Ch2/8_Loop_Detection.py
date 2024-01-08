# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop
# DEFINITION:
# Circular Linked List: A (corrupt) linked list in which a nodes next pointer points to an earlier node,
# so as to make a loop in the linked list.
# EXAMPLE:
# Input: A -> B -> C -> D -> E -> C[the same C as earlier]
# Output: C
# Intersection: Given two singly linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node(by reference) as the jth node of the second
# linked list, then they are intersecting.

from LinkedList import LinkedList,Node
import unittest
#-------------------------------------------------------------

def get_circular_startpoint(cll):
    if not cll.head or cll.next.head:
        return None
    
    return None

#-------------------------------------------------------------
# Time: 
# Space:
#-------------------------------------------------------------
cll = LinkedList()
cll.group_add([1,2,3,4,5,6])

curr = cll.head
while curr.next:        #last reference
    curr = curr.next

curr2 = cll.head
while curr2.value != 3: #Chose a reference to circle back to
    curr2 = curr2.next

curr.next = curr2.next  #Set last reference to the starting point of the CLL

curr2 = cll.head
for _ in range(50):       #print the CLL a certain amount of times
    print(curr2.value)
    curr2 = curr2.next

# class Test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()
