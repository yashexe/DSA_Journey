# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

import unittest
#-------------------------------------------------------------

def compress_string(s):
    if len(s) <= 2:
        return s
    
    compressed_str = ''
    i = 1
    curr_char = s[0]
    count = 1

    while i < len(s):
        if curr_char != s[i]:
            compressed_str = compressed_str + curr_char + str(count)
            curr_char = s[i]
            count = 1
            if i == len(s) - 1:
                compressed_str = compressed_str + curr_char + str(1)
        else:
            count += 1
            if i == len(s) - 1:
                compressed_str = compressed_str + curr_char + str(count)

        i += 1
    return compressed_str if len(compressed_str) < len(s) else s


#-------------------------------------------------------------
# Time: 
# Space: 
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def test_one_char(self):
        answer = compress_string('a')
        expected = 'a'
        self.assertEqual(answer, expected)
    
    def test_two_char(self):
        answer = compress_string('aa')
        expected = 'aa'
        self.assertEqual(answer, expected)

if __name__ == '__main__':
    unittest.main()