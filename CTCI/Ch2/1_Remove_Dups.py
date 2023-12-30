# Remove Dups: Write code to remove duplicates from an unsorted linked list.

# FOLLOW-UP: How would you solve this problem if a temporary buffer is not allowed?
from LinkedList import LinkedList,Node
import unittest

#-------------------------------------------------------------

def Remove_Dups(sll):
    if sll.is_empty() or sll.head.next is None:
        return sll

    values_set = set([sll.head.value])

    curr = sll.head

    while curr.next:
        
        if curr.next.value not in values_set:
            values_set.add(curr.next.value)
            curr = curr.next
        else:
            curr.next = curr.next.next

    return sll 

#-------------------------------------------------------------
# Time: O(n) - Iterating through loop once
# Space: O(k) - all unique Node Values
#-------------------------------------------------------------
# What if there is no buffer(eg.A set or dictionary)?
#-------------------------------------------------------------

def Remove_Dups_2(sll):
    if sll.is_empty() or sll.head.next is None:
        return sll

    curr = sll.head

    while curr:
        runner = curr

        while runner.next:
            if curr.value == runner.next.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next

    return sll

#-------------------------------------------------------------
# Time: O(n^2) - Iterating through loop once for every value
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
    #No Buffer
    def test_no_sll_2(self):
        test = LinkedList()
        Remove_Dups_2(test)
        self.assertEqual(test.to_list(),[])

    def test_singular_node_2(self):
        test = LinkedList()
        test.group_add([1])
        Remove_Dups_2(test)
        self.assertEqual(test.to_list(),[1])

    def test_singular_dup_start_2(self):
        test = LinkedList()
        test.group_add([1,1,2])
        Remove_Dups_2(test)
        self.assertEqual(test.to_list(),[1,2])

    def test_singular_dup_end_2(self):
        test = LinkedList()
        test.group_add([1,2,2])
        Remove_Dups_2(test)
        self.assertEqual(test.to_list(),[1,2])

    def test_multiple_dup_2(self):
        test = LinkedList()
        test.group_add([1,1,2,3,3,4,5,5])
        Remove_Dups_2(test)
        self.assertEqual(test.to_list(),[1,2,3,4,5])

    def test_no_dup_2(self):
        test = LinkedList()
        test.group_add([1,2,3,4,5])
        Remove_Dups_2(test)
        self.assertEqual(test.to_list(),[1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()