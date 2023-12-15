# Check Permutation:Given two strings, write a method to
# decide if one is a permutation of the other.
import unittest
#-------------------------------------------------------------

def isPermutation(s1, s2):

    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False
    
    return sorted(s1) == sorted(s2)
#-------------------------------------------------------------
# Time: O(n), Depends on length of str, because of sorted fn.
# Space: O(n), ^

class Test(unittest.TestCase):
    def test_not_str_1(self):
        self.assertFalse(isPermutation('','abc'))

    def test_not_str_2(self):
        self.assertFalse(isPermutation('abc',''))

    def test_not_str_3(self):
        self.assertFalse(isPermutation('',''))

    def test_diff_length(self):
        self.assertFalse(isPermutation('abcd','abc'))

    def test_sorted_true(self):
        self.assertTrue(isPermutation('abc','abc'))

    def test_sorted_false(self):
        self.assertFalse(isPermutation('abc','abd'))

if __name__ == '__main__':
    unittest.main()