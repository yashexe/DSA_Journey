# Remove Dups: Write code to remove duplicates from an unsorted linked list.

# FOLLOW-UP: How would you solve this problem if a temporary buffer is not allowed?
from LinkedList import LinkedList,Node
import unittest

#-------------------------------------------------------------

def Remove_Dups(sll):
    if sll.is_empty() or sll.head.next is None:
        return sll

    values_set = set()

    dummy = Node(0)
    dummy.next = sll.head

    while dummy.next:
        
        if dummy.next.value not in values_set:
            values_set.add(dummy.next.value)
            dummy = dummy.next
        else:
            dummy.next = dummy.next.next

    return sll 

#-------------------------------------------------------------
# Time: O(n) - Iterating through loop once
# Space: O(k) - all unique Node Values
#-------------------------------------------------------------

class test(unittest.TestCase):

    def test_no_sll(self):
        test = LinkedList()
        Remove_Dups(test)
        self.assertEqual(test.to_list(),[])

    def test_singular_node(self):
        test = LinkedList()
        test.group_add([1])
        Remove_Dups(test)
        self.assertEqual(test.to_list(),[1])

    def test_singular_dup_start(self):
        test = LinkedList()
        test.group_add([1,1,2])
        Remove_Dups(test)
        self.assertEqual(test.to_list(),[1,2])

    def test_singular_dup_end(self):
        test = LinkedList()
        test.group_add([1,2,2])
        Remove_Dups(test)
        self.assertEqual(test.to_list(),[1,2])

    def test_multiple_dup(self):
        test = LinkedList()
        test.group_add([1,1,2,3,3,4,5,5])
        Remove_Dups(test)
        self.assertEqual(test.to_list(),[1,2,3,4,5])

    def test_no_dup(self):
        test = LinkedList()
        test.group_add([1,2,3,4,5])
        Remove_Dups(test)
        self.assertEqual(test.to_list(),[1,2,3,4,5])


if __name__ == '__main__':
    unittest.main()