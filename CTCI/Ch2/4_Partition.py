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

    curr = sll.head
    x_in_list = (curr.value == x)

    while curr.next:
        if not x_in_list and curr.next.value == x:
            x_in_list = True
            
        if curr.next.value < x:
            new_node = Node(curr.next.value)

            curr.next = curr.next.next

            new_node.next = sll.head

            sll.head = new_node
        else:
            curr = curr.next

    if x_in_list == False:
        curr = sll.head

        while curr:
            if curr.next.value > x:
                new_node = Node(x)
                new_node.next = curr.next
                curr.next = new_node

                break

            curr = curr.next

    return sll


sll = LinkedList()
sll.group_add([5,3,8,10,2,1,4,2,1,3,2,5,10,101,92,3])
new_sll = partition(sll,5)
print(new_sll)
#-------------------------------------------------------------
# Time:
# Space:
#-------------------------------------------------------------
# class test(unittest.TestCase):


# if __name__ == '__main__':
#     unittest.main()