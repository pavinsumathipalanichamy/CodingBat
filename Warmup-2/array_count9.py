'''
Given an array of ints, 
return the number of 9's in the array.
array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''

# Code
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

print(array_count9([1, 2, 9])) # → 1	1	OK	
print(array_count9([1, 9, 9])) # → 2	2	OK	
print(array_count9([1, 9, 9, 3, 9])) # → 3	3	OK	
print(array_count9([1, 2, 3])) # → 0	0	OK	
print(array_count9([])) # → 0	0	OK	
print(array_count9([4, 2, 4, 3, 1])) # → 0	0	OK	
print(array_count9([9, 2, 4, 3, 1])) # → 1	1	OK