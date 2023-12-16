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
        print('now checking', char)
        if char not in s1:
            print('not in',s1)
            count += 1
            if count > 1:
                print('more than one difference', s1,s2)
                return False
        elif s1Dict[char] == 0:
            print('no more', char, 'left')
            return False
        else:
            s1Dict[char] -= 1
            print('\'', char, '\' removed, ', s1Dict[char], 'left')
    return True
#-------------------------------------------------------------

print(one_away('pale','ple'))
print(one_away('pales','pale'))
print(one_away('pale','bale'))
print(one_away('pale','bake'))
print(one_away('pale','lle'))