# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a
# strictly "first in, first out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter, or they can select whether
# they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data structures
# to maintain this system and implement operations such as enqueue, dequeueAny,
# dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.

import unittest
#-------------------------------------------------------------
class Pet:
    def __init__(self, pet, id, next = None,):
        self.pet = pet
        self.id = id
        self.next = next

class Animal_Shelter:
    def __init__(self):
        self.newest = None
        self.oldest = None

    def enqueue(self,pet,id):
        new_pet = Pet(pet,id)
        if self.is_empty():
            self.newest = self.oldest = new_pet
        else:
            self.newest.next = new_pet
            self.newest = new_pet

    def dequeue_any(self):
        if self.is_empty():
            return None

        adoptee = self.oldest.pet
        self.oldest = self.oldest.next
        return adoptee

    def dequeue_dog(self):
        if self.is_empty():
            return None
        elif self.oldest.id == 'dog':
            return self.dequeue_any()
        
        curr = self.oldest

        while curr.next and curr.next.id != 'dog':
            curr = curr.next
        if curr.next is None:
            return None
        
        adoptee = curr.next.pet
        curr.next = curr.next.next

        return adoptee

    def dequeue_cat(self):
        if self.is_empty():
            return None
        elif self.oldest.id == 'cat':
            return self.dequeue_any()
        
        curr = self.oldest

        while curr.next and curr.next.id != 'cat':
            curr = curr.next
        if curr.next is None:
            return None
        
        adoptee = curr.next.pet
        curr.next = curr.next.next

        return adoptee

    def is_empty(self):
        return self.oldest is None
#-------------------------------------------------------------
# Time: O(1), O(n) - for dequeue_dog/cat
# Space: O(1)
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def test_enqueue_and_dequeue_any(self):
        shelter = Animal_Shelter()
        shelter.enqueue('Buddy', 'dog')
        shelter.enqueue('Whiskers', 'cat')
        shelter.enqueue('Max', 'dog')

        self.assertEqual(shelter.dequeue_any(), 'Buddy')
        self.assertEqual(shelter.dequeue_any(), 'Whiskers')
        self.assertEqual(shelter.dequeue_any(), 'Max')
        self.assertIsNone(shelter.dequeue_any())

    def test_enqueue_and_dequeue_dog(self):
        shelter = Animal_Shelter()
        shelter.enqueue('Buddy', 'dog')
        shelter.enqueue('Whiskers', 'cat')
        shelter.enqueue('Max', 'dog')

        self.assertEqual(shelter.dequeue_dog(), 'Buddy')
        self.assertEqual(shelter.dequeue_dog(), 'Max')
        self.assertIsNone(shelter.dequeue_dog())

    def test_enqueue_and_dequeue_cat(self):
        shelter = Animal_Shelter()
        shelter.enqueue('Buddy', 'dog')
        shelter.enqueue('Whiskers', 'cat')
        shelter.enqueue('Max', 'dog')

        self.assertEqual(shelter.dequeue_cat(), 'Whiskers')
        self.assertIsNone(shelter.dequeue_cat())
        
if __name__ == '__main__':
    unittest.main()