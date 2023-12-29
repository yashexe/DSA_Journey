# Remove Dups: Write code to remove duplicates from an unsorted linked list.

# FOLLOW-UP: How would you solve this problem if a temporary buffer is not allowed?
from LinkedList import LinkedList,Node
import unittest

#-------------------------------------------------------------
def Remove_Dups(sll):
    temp = sll.head
    valDict = {}

    dummy = Node(0)
    dummy.next = sll.head

    while temp:
        valDict[str(temp.value)] = valDict.get(str(temp.value), 0) + 1
        temp = temp.next


    while dummy.next:
        if valDict[str(dummy.next.value)] > 1:
            valDict[str(dummy.next.value)] -= 1
            sll.delete(dummy.next.value)

        dummy = dummy.next

    return sll

test = LinkedList()
test.add(1)
test.add(3)
test.add(7)
test.add(7)
test.add(1)
print(test)
Remove_Dups(test)

print(test)

#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

# class test(unittest.TestCase):
        
# if __name__ == '__main__':
#     unittest.main()