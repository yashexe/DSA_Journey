# Is Unique: Implement an algorithm to determine if a string has all unique characters.

#---------------------------------------------------------------------
def isUnique(s):
    if len(s) > 128: 
        return False # Assuming ASCII

    uniqueChar = {}

    for char in s:
        if char in uniqueChar:
            return False
        
        uniqueChar[char] = 1

    return True

#Time: O(n)
#Space: O(min(n,d)) either length of string or # distinct characters

print(isUnique('debr!@#$%^&*sfwv3'))

#----------------------------------------------------------------------
# What if you cannot use additional data structures?
#-----------------------------------------------------------------------

def noDS(s):
    if len(s) > 128:
        return False # Assuming ASCII

    sorted_s = sorted(s)

    for i in range(len(s) - 1):
        if sorted_s[i] == sorted_s[i+1]:
            return False
    
    return True

#Time: O(n)
#Space: O(1)

print(noDS('debr!@#$%^&*sfwv3'))
