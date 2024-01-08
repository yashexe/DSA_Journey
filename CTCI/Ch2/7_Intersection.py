# Intersection: Given two singly linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node(by reference) as the jth node of the second
# linked list, then they are intersecting.

from LinkedList import LinkedList,Node
import unittest
#-------------------------------------------------------------

def is_intersection(sll1,sll2):
    if not sll1.head or not sll2.head:
        return None
    if sll1.head == sll2.head:
        return sll1.head
    
    node_set = set([sll1.head,sll2.head])

    if sll1.length() > sll2.length():
        curr1 = sll1.head
        curr2 = sll2.head
    else:
        curr1 = sll2.head
        curr2 = sll1.head

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
# Time: O(min(m,n)) - travserse all nodes if none are intersection
# Space: O(m + n) - set stores all nodes if none are intersection
#-------------------------------------------------------------
sll1 = LinkedList()
sll2 = LinkedList()
sll3 = LinkedList()
sll4 = LinkedList()
sll1.group_add([1,2,3])
sll2.group_add([7,8,9])
sll3.group_add([4,5,6])
sll4.group_add([10,11,12,4,5,6])

curr = sll1.head
curr2 = sll2.head
curr3 = sll4.head

while curr.next:
    curr = curr.next
curr.next = sll3.head

while curr2.next:
    curr2 = curr2.next
curr2.next = sll3.head

while curr3.next.value != 4:
    curr3 = curr3.next

print(is_intersection(sll1,sll4))
print(is_intersection(sll1,sll2))
# class test(unittest.TestCase):


# if __name__ == '__main__':
#     unittest.main()