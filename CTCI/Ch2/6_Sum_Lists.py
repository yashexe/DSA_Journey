# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at the head of the
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE:
# INPUT: 7->1->6 + 5->9->2
# Output: 2->1->9
# Assume numbers do not have leading zeros, and exist eg. 20 + 024, 20 + None
from LinkedList import LinkedList,Node
import unittest
#-------------------------------------------------------------

def sum_sll(list1,list2):

    addend1 = list1.head
    addend2 = list2.head
    
    while addend1:
        addend2.value += addend1.value

        if addend2.value >= 10:
            addend2.value -= 10

            if addend2.next:
                addend2.next.value += 1
            else:
                addend2.next = Node(1)
        
        if not addend2.next and addend1.next:
            addend2.next = Node(0)
        
        addend1 = addend1.next
        addend2 = addend2.next

    return list2
#-------------------------------------------------------------
# Time:  O(max(m, n))
# Space:  O(1)
#-------------------------------------------------------------
# FOLLOW UP: Suppose the digits are stored in forward order. Repeat the above problem.
# INPUT: 6->1->7 + 2->9->5
# Output: 9->1->2
#-------------------------------------------------------------

def sum_sll2(list1,list2):
    if list1.head.value == 0 and list2.head.value == 0:
        return list1
    elif list1.head.value == 0 and list2.head.value != 0:
        return list2
    elif list1.head.value != 0 and list2.head.value == 0:
        return list1

    if list1.length() > list2.length():
        sll1 = list1.head
        sll2 = list2.head
    else:
        sll1 = list2.head
        sll2 = list1.head
    
    if list1.length() != list2.length():
        zeros = LinkedList()

        for i in range(abs(list1.length() - list2.length())):
            zeros.add(0)
        curr = zeros.head

        while curr.next:
            curr = curr.next
        curr.next = sll2
        sll2 = zeros.head
    
    result = 0
    while sll1 and sll2:
        result = result*10 + sll1.value + sll2.value
        sll1 = sll1.next
        sll2 = sll2.next

    sum = LinkedList()
    sum.group_add([int(i) for i in str(result)])
    
    return sum
#-------------------------------------------------------------
# Time:  O(max(m, n))
# Space: O(m + n)
#-------------------------------------------------------------
class test(unittest.TestCase):
    def test_zero_lists(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.add(0)
        list2.add(0)

        sum1 = sum_sll(list1,list2).to_list()
        sum2 = sum_sll2(list1,list2).to_list()

        self.assertEqual(sum1,[0])
        self.assertEqual(sum2,[0])
    def test_carry(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.group_add([4,2,7])
        list2.group_add([9,4])

        sum1 = sum_sll(list1,list2).to_list()

        list3 = LinkedList()
        list4 = LinkedList()
        list3.group_add([7,2,4])
        list4.group_add([4,9])

        sum2 = sum_sll2(list3,list4).to_list()

        self.assertEqual(sum1,[3,7,7])
        self.assertEqual(sum2,[7,7,3])
    def test_carry_flipped(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.group_add([9,4])
        list2.group_add([4,2,7])

        sum1 = sum_sll(list1,list2).to_list()

        list3 = LinkedList()
        list4 = LinkedList()
        list3.group_add([4,9])
        list4.group_add([7,2,4])

        sum2 = sum_sll2(list3,list4).to_list()

        self.assertEqual(sum1,[3,7,7])
        self.assertEqual(sum2,[7,7,3])
    def test_incr_digits(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.group_add([9,9,9])
        list2.group_add([1])

        sum1 = sum_sll(list1,list2).to_list()

        list3 = LinkedList()
        list4 = LinkedList()
        list3.group_add([9,9,9])
        list4.group_add([1])

        sum2 = sum_sll2(list3,list4).to_list()

        self.assertEqual(sum1,[0,0,0,1])
        self.assertEqual(sum2,[1,0,0,0])

if __name__ == '__main__':
    unittest.main()