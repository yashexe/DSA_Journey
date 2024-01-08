# Intersection: Given two singly linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node(by reference) as the jth node of the second
# linked list, then they are intersecting.

from LinkedList import LinkedList,Node
import unittest
#-------------------------------------------------------------

def get_intersection(sll1,sll2):
    if not sll1.head or not sll2.head:
        return None
    if sll1.head == sll2.head:
        return sll1.head
    
    node_set = set([sll1.head,sll2.head])

    if sll1.length() > sll2.length():
        curr1, curr2 = sll1.head, sll2.head
    else:
        curr1, curr2 = sll2.head, sll1.head

    while curr1.next:
    
        if curr1.next in node_set:
            return curr1.next
        else:
            node_set.add(curr1.next)

        if curr2 and curr2.next in node_set:
            return curr2.next
        elif curr2:
            node_set.add(curr2.next)

        curr1 = curr1.next
        if curr2:
            curr2 = curr2.next
    return None

#-------------------------------------------------------------
# Time: O(min(m,n))
# Space: O(m + n) - set stores all nodes if none are intersection
#-------------------------------------------------------------

class test(unittest.TestCase):
    def test_empty_sll(self):
        sll1 = LinkedList()
        sll2 = LinkedList()
        self.assertEqual(get_intersection(sll1, sll2), None)

    def test_no_intersection(self):
        sll1 = LinkedList()
        sll1.group_add([1, 2, 3])
        sll2 = LinkedList()
        sll2.group_add([4, 5, 6])
        self.assertEqual(get_intersection(sll1, sll2), None)

    def test_intersection_at_beginning(self):
        common_node = Node(7)
        sll1 = LinkedList()
        sll1.group_add([1, 2, 3])
        sll1.head.next.next.next = common_node
        sll2 = LinkedList()
        sll2.head = common_node
        self.assertEqual(get_intersection(sll1, sll2), common_node)

    def test_intersection_in_middle(self):
        common_node = Node(7)
        sll1 = LinkedList()
        sll1.group_add([1, 2, 3, 4])
        sll1.head.next.next.next.next = common_node
        sll1.group_add([8, 9])
        sll2 = LinkedList()
        sll2.group_add([5, 6])
        sll2.head.next.next = common_node
        self.assertEqual(get_intersection(sll1, sll2), common_node)

    def test_intersection_at_end(self):
        common_node = Node(7)
        sll1 = LinkedList()
        sll1.group_add([1, 2, 3])
        sll1.group_add([8, 9])
        sll1.head.next.next.next.next = common_node
        sll2 = LinkedList()
        sll2.group_add([4, 5, 6])
        sll2.head = common_node
        self.assertEqual(get_intersection(sll1, sll2), common_node)

if __name__ == '__main__':
    unittest.main()
