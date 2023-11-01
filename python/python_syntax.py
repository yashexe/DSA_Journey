# range vs enumerate

numbers = [1,2,3,4,5]

for i in range(len(numbers)):       #need access to len(nums) for this
    print(numbers[i],i)         

for i, elem in enumerate(numbers):
    print(elem)