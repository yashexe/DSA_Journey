# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a
# strictly "first in, first out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter, or they can select whether
# they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data structures
# to maintain this system and implement operations such as enqueue, dequeueAny,
# dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.

import unittest
#-------------------------------------------------------------
class Node:
    def __init__(self, pet, id, next = None,):
        self.pet = pet
        self.id = id
        self.next = next

class Animal_Shelter:
    def __init__(self):
        self.newest = None
        self.oldest = None

    def enqueue(self,pet,id):
        pass

    def dequeue_any(self):
        pass

    def dequeue_dog(self):
        pass

    def dequeue_cat(self):
        pass
#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------
    
# class Test(unittest.TestCase):

# if __name__ == '__main__':
#     unittest.main()