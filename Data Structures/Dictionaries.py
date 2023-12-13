# Dictionary is a 'key : value' pair

##Requirements##
# keys are unique
# written with {}, comma separated pairs
#indexed by keys(any type)
    # tuples can be used as keys if they contain only strings numbers or tuples

##Operations##
# initialization
myDict = { 'jack': 1}
# storing value with some key
myDict['slam'] = 65
# extracting a value, given a key
print(myDict['slam'])
# replacing values, given a key in use
myDict['slam'] = 66
# delete key
del myDict['jack']
# print all pairs in inserted order
print(list(myDict))
# print all pairs in sorted order
print(sorted(myDict))
# check if a single key exists/doesnt exist
print('slam' in myDict)
print('slam' not in myDict)

##Errors##
#Extracting a value with a non-existent key