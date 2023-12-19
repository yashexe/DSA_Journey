# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

import unittest
#-------------------------------------------------------------
def one_away(s1,s2):
    if abs(len(s1) - len (s2)) > 1:
        return False
    elif len(s1) == len(s2):
        return eq_str_len(s1,s2)
    else:
        return insert_removal(s1,s2)

def eq_str_len(s1,s2):
    count = 0
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            count +=1
            if count > 1:
                return False
    return True

def insert_removal(s1,s2):
    count = 0

    shorter, longer = (s1, s2) if len(s1) < len(s2) else (s2, s1)

    shorterDict = {char: shorter.count(char) for char in set(shorter)}
    
    for char in longer:
        if char not in shorterDict:
            count +=1
            if count > 1:
                return False
        else:
            shorterDict[char] -= 1    
    return True

# Time: O(max(len(s1),len(s2)))
# Space:O(min(len(s1),len(s2)))
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def test_general_true_1(self):
        self.assertTrue(one_away('place','plxce'))
    def test_general_true_2(self):
        self.assertTrue(one_away('place','places'))
    def test_general_true_3(self):
        self.assertTrue(one_away('place','plac'))

    def test_general_false_4(self):
        self.assertFalse(one_away('place','plxxe'))
    def test_general_false_5(self):
        self.assertFalse(one_away('place','plaxes'))
    def test_general_false_6(self):
        self.assertFalse(one_away('place','plax'))

    def test_long_str(self):
        self.assertFalse(one_away('place','placess'))
    def test_short_str(self):
        self.assertFalse(one_away('place','pla'))

    def test_no_str_1(self):
        self.assertFalse(one_away('','place'))
    def test_no_str_2(self):
        self.assertFalse(one_away('place',''))
    def test_no_str_3(self):
        self.assertTrue(one_away('','')) #0 edits away

    def test_space_1(self):
        self.assertTrue(one_away('place',' place'))
    def test_space_2(self):
        self.assertTrue(one_away('place ','place'))
    def test_space_3(self):
        self.assertTrue(one_away('place','pl ce'))

if __name__ == '__main__':
    unittest.main()