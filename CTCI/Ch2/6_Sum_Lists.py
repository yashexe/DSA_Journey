# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at the head of the
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE:
# INPUT: 7->1->6 + 5->9->2
# Output: 2->1->9

from LinkedList import LinkedList,Node
import unittest
#-------------------------------------------------------------

def sum_sll(list1,list2):
    sum = LinkedList()
    
    num1 = to_int(list1)
    num2 = to_int(list2)

    sum_str = reversed(str(num1 + num2))

    sum.group_add([int(i) for i in sum_str])

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
# Time: 
# Space:
#-------------------------------------------------------------
# FOLLOW UP: Suppose the digits are stored in forward order. Repeat the above problem.
# INPUT: 6->1->7 + 2->9->5
# Output: 9->1->2
#-------------------------------------------------------------

def sum_sll2(list1,list2):
    sum = LinkedList()

    list1_arr = list1.to_list()
    list1_arr = list1.to_list()


    return sum

#-------------------------------------------------------------
# Time: 
# Space:
#-------------------------------------------------------------
# class test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()