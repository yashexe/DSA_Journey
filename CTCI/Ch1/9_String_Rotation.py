# String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings s1 and s2, write code to check if s2 is a rotation of s1, using only one call
# to isSubstring. e.g. 'waterbottle' is a rotation of 'elttobretaw'

import unittest

#-------------------------------------------------------------
def isSubstring(s1,s2):
    return s2 in s1

def String_Rotate(s1,s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    
    return isSubstring(s1 + s1, s2)
    

#-------------------------------------------------------------
# Time: O(n) - 'in' makes isSubString O(mn), though this function isnt tested in this Q
# Space: O(n)
#-------------------------------------------------------------

class test(unittest.TestCase):
    def test_single_char(self):
        self.assertTrue(String_Rotate('s','s'))

    def test_diff_length(self):
        self.assertFalse(String_Rotate('shares','share'))
    
    def test_single_str(self):
        self.assertFalse(String_Rotate('','s'))

    def test_rotation(self):
        self.assertTrue(String_Rotate('waterbottle','erbottlewat'))
        
if __name__ == '__main__':
    unittest.main()