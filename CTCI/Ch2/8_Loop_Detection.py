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
    if not cll.head or not cll.head.next:
        return None
    
    cll_set = set([cll.head])

    curr = cll.head

    while curr.next:

        if curr.next in cll_set:
            return curr.next
        cll_set.add(curr.next)
        curr = curr.next
    return None

#-------------------------------------------------------------
# Time: O(n)
# Space: O(n) - Worst case is n unique nodes 
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def test_no_cycle(self):
        cll = LinkedList()
        cll.group_add([1, 2, 3, 4, 5])
        self.assertEqual(get_circular_startpoint(cll), None)

    def test_cycle_at_beginning(self):
        cll = LinkedList()
        cll.add(10)
        cll.head.next = cll.head
        self.assertEqual(get_circular_startpoint(cll), cll.head)

    def test_cycle_in_middle(self):
        cll = LinkedList()
        cll.group_add([1, 2, 3, 4, 5])
        middle_node = cll.head.next.next 
        cll.head.next.next.next.next.next = middle_node 
        self.assertEqual(get_circular_startpoint(cll), middle_node)

    def test_cycle_at_end(self):
        cll = LinkedList()
        cll.group_add([1, 2, 3, 4, 5])
        end_node = cll.head.next.next.next.next  
        cll.head.next.next.next.next.next = end_node  
        self.assertEqual(get_circular_startpoint(cll), end_node)

if __name__ == '__main__':
    unittest.main()
