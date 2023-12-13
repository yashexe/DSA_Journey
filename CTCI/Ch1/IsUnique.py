def isUnique(word):
    uniqueChar = {}

    for char in word:
        if char in uniqueChar:
            return False
        
        uniqueChar[char] = 1

    return True

print(isUnique('debr!@#$%^&*sfwv3'))

#Time: O(n)
#Space: O(min(n,d))

#Space complexity is either the length of the string, or # of distinct characters