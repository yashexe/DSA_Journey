# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"
import unittest
#-------------------------------------------------------------

def URLify(s,n):
    for i in range(n):

        if s[i] == ' ':
            s = s[:i]  + '%20' + s[i+1:]
            if i - n <= -3:
                i+=3
    return s
#Time: O(n)
#Space: O(max(m)) m is the number of spaces
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def no_space(self):
        expected = 'MrJohnSmith'
        result = URLify('MrJohnSmith',11)
        self.assertEqual(expected, result)

    def space_start(self):
        expected = "%20MrJohnSmith"
        result = URLify(' MrJohnSmith', 12)
        self.assertEqual(expected, result)

    def space_middle_end(self):
        expected = "Mr%20John%20Smith"
        result = URLify('Mr John Smith ', 13)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()