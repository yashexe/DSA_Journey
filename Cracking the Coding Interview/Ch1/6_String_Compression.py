# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

import unittest
#-------------------------------------------------------------

def compress_string_1(s):
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
# Time: O(m*n^2) - string concatenation
# Space: O(n) - worst case is when there are no repeats: eg. abc -> a1b1c1 -> O(2n) = O
#-------------------------------------------------------------
def compress_string_2(s):
    if len(s) <= 2:
        return s
    
    compressed_str = []
    count = 0

    for i in range(len(s)):
        if i != 0 and s[i] != s[i-1]:
            compressed_str.append(s[i-1] + str(count))
            count = 0
        count += 1

    compressed_str.append(s[-1] + str(count))

    return ''.join(compressed_str) if len(compressed_str) < len(s) else s
#-------------------------------------------------------------
# Time: O(n)
# Space: O(n) - worst case is when there are no repeats: eg. abc -> a1b1c1 -> O(2n) = O
#-------------------------------------------------------------

class Test(unittest.TestCase):
    def test_one_char(self):
        answer = compress_string_1('a')
        expected = 'a'
        self.assertEqual(answer, expected)
    
    def test_two_char(self):
        answer = compress_string_1('aa')
        expected = 'aa'
        self.assertEqual(answer, expected)

    def test_starting_distinct_char(self):
        answer = compress_string_1('aabbb')
        expected = 'a2b3'
        self.assertEqual(answer, expected)

    def test_starting_compressable_char(self):
        answer = compress_string_1('aaabbb')
        expected = 'a3b3'
        self.assertEqual(answer, expected)
    
    def test_ending_distinct_char(self):
        answer = compress_string_1('aaaab')
        expected = 'a4b1'
        self.assertEqual(answer, expected)

    def test_ending_compressable_char(self):
        answer = compress_string_1('aabbb')
        expected = 'a2b3'
        self.assertEqual(answer, expected)

    def test_one_char_2(self):
        answer = compress_string_2('a')
        expected = 'a'
        self.assertEqual(answer, expected)
    
    def test_two_char_2(self):
        answer = compress_string_2('aa')
        expected = 'aa'
        self.assertEqual(answer, expected)

    def test_starting_distinct_char_2(self):
        answer = compress_string_2('aabbb')
        expected = 'a2b3'
        self.assertEqual(answer, expected)

    def test_starting_compressable_char_2(self):
        answer = compress_string_2('aaabbb')
        expected = 'a3b3'
        self.assertEqual(answer, expected)
    
    def test_ending_distinct_char_2(self):
        answer = compress_string_2('aaaab')
        expected = 'a4b1'
        self.assertEqual(answer, expected)

    def test_ending_compressable_char_2(self):
        answer = compress_string_2('aabbb')
        expected = 'a2b3'
        self.assertEqual(answer, expected)

if __name__ == '__main__':
    unittest.main()