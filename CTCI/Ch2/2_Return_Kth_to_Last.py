# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

from LinkedList import LinkedList,Node
import unittest

#-------------------------------------------------------------
# ITERATIVE SOLUTION
#-------------------------------------------------------------

def kth_to_last_iterative(sll,k):
    if k > sll.length() or k < 0 or sll is None:
        return None
    
    index = sll.length() - k

    curr = sll.head

    while index != 0:
        curr = curr.next
        index -= 1

    return curr.value
#-------------------------------------------------------------
# Time: O(n) - O(n - k) simplifies to O(n)
# Space: O(n)
#-------------------------------------------------------------
# RECURSIVE SOLUTION
#-------------------------------------------------------------

def kth_to_last_recursive_wrapper(sll,k):
    if sll.head is None or k < 0:
        return None
    
    result, current = kth_to_last_recursive(sll.head,k)

    return result

def kth_to_last_recursive(sll,k):
    if sll is None:
        return None, 0
    
    result,current = kth_to_last_recursive(sll.next,k)
    
    current +=1

    if k == current:
        return sll.value,current

    return result,current
    
#-------------------------------------------------------------
# Time: O(n)
# Space: O(n)
#-------------------------------------------------------------

class test(unittest.TestCase):

    def test_no_sll(self):
        sll = LinkedList()
        self.assertEqual(kth_to_last_iterative(sll,1),None)
        self.assertEqual(kth_to_last_recursive_wrapper(sll,1),None)

    def test_singular_node(self):
        sll = LinkedList()
        sll.add(1)
        self.assertEqual(kth_to_last_iterative(sll,2),None)
        self.assertEqual(kth_to_last_recursive_wrapper(sll,2),None)

    def test_k_negative(self):
        sll = LinkedList()
        sll.group_add([1,2,3,4,5,6])
        self.assertEqual(kth_to_last_iterative(sll,-2),None)
        self.assertEqual(kth_to_last_recursive_wrapper(sll,-2),None)

    def test_k_larger_than_list(self):
        sll = LinkedList()
        sll.group_add([1,2,3,4,5,6])
        self.assertEqual(kth_to_last_iterative(sll,10),None)
        self.assertEqual(kth_to_last_recursive_wrapper(sll,10),None)

    def test_k_first(self):
        sll = LinkedList()
        sll.group_add([1,2,3,4,5,6])
        self.assertEqual(kth_to_last_iterative(sll,1),6)
        self.assertEqual(kth_to_last_recursive_wrapper(sll,1),6)

    def test_k_last(self):
        sll = LinkedList()
        sll.group_add([1,2,3,4,5,6])
        self.assertEqual(kth_to_last_iterative(sll,6),1)
        self.assertEqual(kth_to_last_recursive_wrapper(sll,6),1)

if __name__ == '__main__':
    unittest.main()