# Partition: Write code to partition a linked list around a value x, such that all
# nodes less than x come before all nodes greater than x. If x is contained within
# the list, the values of x only need to be after the elements less than 
# x (see below). The partition element x can appear anywhere in the "right partition";
# it does not need to appear between the left and right partitions.
# EXAMPLE:
# Input: 3->5->8->5->10->2->1 [parition = 5]
# Output: 3->1->2->10->5->5->8

from LinkedList import LinkedList,Node
import unittest
#-------------------------------------------------------------
def partition(sll,x):
    if not sll.head:
        return sll
    
    x_in_list = sll.head.value == x

    curr = sll.head
    
    while curr.next:
        if not x_in_list and curr.next.value == x:
            x_in_list = True

        if curr.next.value < x:
            new_node = Node(curr.next.value)
            new_node.next = sll.head
            sll.head = new_node
            curr.next = curr.next.next
        else:
            curr = curr.next

    if not x_in_list:
        curr = sll.head

        while curr.next and curr.next.value <= x:
            curr = curr.next
    
        new_node = Node(x)
        new_node.next = curr.next
        curr.next = new_node

    return sll

#-------------------------------------------------------------
# Time: O(n)
# Space: O(1) - new nodes created dont necessarily increase w.r.t. size of SLL
#-------------------------------------------------------------
class test(unittest.TestCase):
    def test_partition_empty_list(self):
        sll = LinkedList()
        sll.group_add([])

        expected_result = []
        partitioned_sll = partition(sll, 5)

        self.assertEqual(partitioned_sll.to_list(), expected_result)

    def test_partition_all_values_less_than_x(self):
        sll = LinkedList()
        sll.group_add([3, 2, 1])

        expected_result = [1, 2, 3, 5]
        partitioned_sll = partition(sll, 5)

        self.assertEqual(partitioned_sll.to_list(), expected_result)

    def test_partition_all_values_greater_than_x(self):
        sll = LinkedList()
        sll.group_add([8, 9, 10])
        expected_result = [8, 5, 9, 10]
        partitioned_sll = partition(sll, 5)
        self.assertEqual(partitioned_sll.to_list(), expected_result)

    def test_partition_mixed_values(self):
        sll = LinkedList()
        sll.group_add([3, 8, 2, 10, 1, 5, 7])
        expected_result = [1, 2, 3, 8, 10, 5, 7]
        partitioned_sll = partition(sll, 5)
        self.assertEqual(partitioned_sll.to_list(), expected_result)

    def test_partition_x_at_the_end(self):
        sll = LinkedList()
        sll.group_add([3, 8, 2, 10, 1, 5, 7, 6])
        expected_result = [5, 1, 2, 3, 8, 10, 7, 6]
        partitioned_sll = partition(sll, 6)
        self.assertEqual(partitioned_sll.to_list(), expected_result)
if __name__ == '__main__':
    unittest.main()