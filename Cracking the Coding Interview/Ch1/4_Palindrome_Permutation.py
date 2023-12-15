# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)
import unittest
#-------------------------------------------------------------

def check_palindrome_permutation(s):
    if not s:
        return False
    
    charDict = {}
    oddCount = 0
    dictSize = 0

    for char in s:
        if char == ' ':
            continue
        else:
            charDict[char] = charDict.get(char, 0) + 1

    for char in charDict:
        dictSize += charDict[char]

    for char in charDict:
        if oddCount > 1:
            return False
        if charDict[char] == 1:
            if dictSize % 2 == 0:
                return False
            oddCount +=1
                
    return True
#Time: O(n) -> n + n + n iterations of for-loop -> 3n -> n
#Space: O(n), Worst case, all char are unique
class Test(unittest.TestCase):
    def test_no_str(self):
        self.assertFalse(check_palindrome_permutation(''))

    def test_single_char(self):
        self.assertTrue(check_palindrome_permutation('a'))

    def test_spacing(self):
        self.assertTrue('Tact Coa')

    def test_spacing_2(self):
        self.assertFalse(check_palindrome_permutation(' Tact Coa t '))

    def test_general_1(self):
        self.assertTrue(check_palindrome_permutation('yashhsay'))

    def test_general_2(self):
        self.assertFalse(check_palindrome_permutation('yashbsay'))

if __name__ == '__main__':
    unittest.main()