# Palindrome: Implement a function to check if a linked list is a palindrome.

from LinkedList import LinkedList,Node
import unittest
#-------------------------------------------------------------

def is_palindrome(sll):
    if not sll.head or not sll.head.next:
        return True

    reversed_arr = to_reversed_array(sll.head, [])

    return sll.to_list() == reversed_arr

def to_reversed_array(sll,result):
    if sll.next != None:
        result = to_reversed_array(sll.next,result)

    result.append(sll.value)
    return result

sll = LinkedList()
sll.group_add([1,2,3,2,1])

print(is_palindrome(sll))
#-------------------------------------------------------------
# Time: O(n)
# Space: O(n)
#-------------------------------------------------------------
class test(unittest.TestCase):

    def test_empty_list(self):
        sll = LinkedList()
        self.assertTrue(is_palindrome(sll))

    def test_single_element_list(self):
        sll = LinkedList()
        sll.add(1)
        self.assertTrue(is_palindrome(sll))

    def test_palindrome_list(self):
        sll = LinkedList()
        sll.group_add([1, 2, 3, 2, 1])
        self.assertTrue(is_palindrome(sll))

    def test_non_palindrome_list(self):
        sll = LinkedList()
        sll.group_add([1, 2, 3, 4, 5])
        self.assertFalse(is_palindrome(sll))

    def test_odd_length_palindrome_list(self):
        sll = LinkedList()
        sll.group_add([1, 2, 3, 3, 2, 1])
        self.assertTrue(is_palindrome(sll))

    def test_odd_length_non_palindrome_list(self):
        sll = LinkedList()
        sll.group_add([1, 2, 3, 4, 5, 6, 7])
        self.assertFalse(is_palindrome(sll))
if __name__ == '__main__':
    unittest.main()