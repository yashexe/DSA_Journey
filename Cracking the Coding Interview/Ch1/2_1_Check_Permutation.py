# Check Permutation:Given two strings, write a method to
# decide if one is a permutation of the other.

#This is originally written with the assumption that the question is asking if one is in another
#-------------------------------------------------------------
import unittest

def isPermutation(s1,s2):
    if not s1 or not s2:
        return False

    if len(s1) == len(s2): 
        return s1 == s2

    shorter, longer = (s1, s2) if len(s1) < len(s2) else (s2, s1)

    n = 0
    for i,char in enumerate(longer):
        if char == shorter[n]:
            n += 1
            if n == len(shorter):
                return True
        elif char == shorter[0]:
            n = 1
        else:
            n = 0
            
    return False
# Time: O(max(m,n)), worst case will loop through the longer string
# Space: O(1)

#-------------------------------------------------------------

class Test(unittest.TestCase):
    def test_permutation(self):
        self.assertTrue(isPermutation("asdf", "qwertyuiopasdfghjklzxcvbnm1234567890"))

    def test_not_permutation(self):
        self.assertFalse(isPermutation("asdd", "qwertyuiopasdfghjklzxcvbnm1234567890"))

    def test_empty_str_1(self):
        self.assertFalse(isPermutation("asdf", ""))

    def test_empty_str_2(self):
        self.assertFalse(isPermutation("", "qwertyuiopasdfghjklzxcvbnm1234567890"))

    def test_empty_str_3(self):
        self.assertFalse(isPermutation("", ""))

    def test_equal_length_1(self):
        self.assertTrue(isPermutation("asdf", "asdf"))

    def test_equal_length_2(self):
        self.assertFalse(isPermutation("asdf", "aadf"))

if __name__ == '__main__':
    unittest.main()