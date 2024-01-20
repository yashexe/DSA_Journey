# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single
# digit. Add the two numbers and return the sum as a linked list. You may assume the
# two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1, l2):
    addend = l2
        
    while l1:
        addend.val += l1.val

        if addend.val >= 10:
            addend.val -= 10

            if addend.next: addend.next.val += 1
            else:
                addend.next = ListNode(1)
            
        if not addend.next and l1.next: addend.next = ListNode(0)
            
        l1 = l1.next
        addend = addend.next
        
    while addend:
        if addend.val == 10:
            addend.val %= 10

            if addend.next: addend.next.val += 1
            else:
                addend.next = ListNode(1)
                break
                
            addend = addend.next

        else: break
    return l2