# Given a string s, find the length of the longest 
# substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    count = 0
    longest = 0
    i = 0

    s_dict = {}
    while i < len(s):
        if s[i] in s_dict:
            count = 1
            i = s_dict[s[i]] + 1
            s_dict = {s[i]: i}
        else:
            count += 1
            s_dict[s[i]] = i
            
            if count >= longest:
                longest = count

        i += 1

    return longest

