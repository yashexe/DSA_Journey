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
    
    count = 0
    s1Dict = {}
    for char in s1:
        s1Dict[char] = s1Dict.get(char,0) + 1
    
    for char in s2:

        if char not in s1 or s1Dict[char] == 0:
            print(char, 'not in',s1)
            count += 1
            if count > 1 or (count == 1 and len(s1) != len(s2)):
                return False
        else:
            s1Dict[char] -= 1
            print('\'', char, '\' removed, ', s1Dict[char], 'left')
    
    if count >= 1 and len(s1) == len(s2) or (count == 0 and len(s1) != len(s2)):
        return True

    return False
#-------------------------------------------------------------

# print('pale','ple',one_away('pale','ple'))
# print('ple','pale',one_away('ple','pale'))
# print('pales','pale',one_away('pales','pale'))
# print('pale','pales',one_away('pale','pales'))
# print('pale','bale',one_away('pale','bale'))
# print('pale','bake',one_away('pale','bake'))
print('pale','lle',one_away('pale','lle'))
print('lle','pale',one_away('lle','pale'))
print('alle','pale',one_away('alle','pale'))
print('pale','alle',one_away('pale','alle'))