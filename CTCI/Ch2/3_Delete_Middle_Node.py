# Delete Middle Node: Implement an algorithm to delete a node in the middle (ie., any
# any node but the first and last node, not necessarily the middle) of a singly linked
# list, given only access to that node
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list is a->b->d->e->f

from LinkedList import LinkedList,Node
import unittest
#-------------------------------------------------------------
# If given node value
#-------------------------------------------------------------
def delete_middle_value(sll,element):
    if sll.head.value == element:
        return
    
    sll_length = sll.length()
    curr_length = 1

    curr = sll.head

    while curr.next and curr_length + 1 != sll_length:
        if curr.next.value == element:
            curr.next = curr.next.next
            return
        curr = curr.next
        curr_length+=1

#-------------------------------------------------------------
# Time: O(n)
# Space: O(1)
#-------------------------------------------------------------
# If given node 
#-------------------------------------------------------------
def delete_middle_node(node):
    if node is None or node.next is None:
        return
    node.value = node.next.value
    node.next = node.next.next
#-------------------------------------------------------------
# Time: O(1)
# Space: O(1)
#-------------------------------------------------------------
class test(unittest.TestCase):

    def test_first_element(self):
        sll = LinkedList()
        sll.group_add([1,2,3,4,5,6])
        delete_middle_value(sll,1)

        sll_2 = LinkedList()
        node = sll_2.add(1)
        sll_2.group_add([2,3,4,5,6])
        delete_middle_node(node)

        self.assertEqual(sll_2.to_list(),[1,2,3,4,5,6])

    def test_last_element(self):
        sll = LinkedList()
        sll.group_add([1,2,3,4,5,6])
        delete_middle_value(sll,6)

        sll_2 = LinkedList()
        sll_2.group_add([1,2,3,4,5])
        node = sll_2.add(6)
        delete_middle_node(node)

        self.assertEqual(sll.to_list(),[1,2,3,4,5,6])
        self.assertEqual(sll_2.to_list(),[1,2,3,4,5,6])

    def test_middle_element(self):
        sll = LinkedList()
        sll.group_add([1,2,3,4,5,6])
        delete_middle_value(sll,3)

        sll_2 = LinkedList()
        sll_2.group_add([1,2])
        node = sll_2.add(3)
        sll_2.group_add([4,5,6])
        delete_middle_node(node)

        self.assertEqual(sll.to_list(),[1,2,4,5,6])
        self.assertEqual(sll_2.to_list(),[1,2,4,5,6])

if __name__ == '__main__':
    unittest.main()