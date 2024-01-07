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
    sum = LinkedList()
    
    num1 = to_int(list1)
    num2 = to_int(list2)

    sum.group_add([int(i) for i in reversed(str(num1 + num2))])

    return sum

def to_int(list):
    num = 0
    i = 0
    curr = list.head

    while curr:
        num += curr.value*pow(10,i)
        i += 1
        curr = curr.next

    return num

#-------------------------------------------------------------
# Time:  O(max(m, n))
# Space:  O(max(m, n))
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
    
    sum = LinkedList()
        
    list1_arr = list1.to_list()
    list2_arr = list2.to_list()

    sum_str = str(int(''.join(map(str,list1_arr))) + int(''.join(map(str,list2_arr))))

    sum.group_add([int(i) for i in sum_str])

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
    def test_incr_digits(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.add(1)
        list2.add(9)

        sum1 = sum_sll(list1,list2).to_list()
        sum2 = sum_sll2(list1,list2).to_list()

        self.assertEqual(sum1,[0,1])
        self.assertEqual(sum2,[1,0])

if __name__ == '__main__':
    unittest.main()