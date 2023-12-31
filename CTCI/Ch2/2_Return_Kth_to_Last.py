# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

from LinkedList import LinkedList,Node
import unittest

#-------------------------------------------------------------

def kth_to_last(sll,k):
    curr = sll.head
    sll_length = 0

    while curr:
        sll_length += 1
        curr = curr.next

    if k > sll_length:
        return None

    curr = sll.head

    while sll_length != k and curr:
        curr = curr.next
        sll_length -= 1

    return curr.value 

sll = LinkedList()
sll.group_add([1,2,3,4,5])
print(kth_to_last(sll,3))

#-------------------------------------------------------------
# Time:
# Space:
#-------------------------------------------------------------

# class test(unittest.TestCase):



# if __name__ == '__main__':
#     unittest.main()