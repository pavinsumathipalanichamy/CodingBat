'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3 
appears in the array somewhere.
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''

# Code 
def array123(nums):
  if len(nums) < 3:
    return False
  for i in range(0, len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

print(array123([1, 1, 2, 3, 1])) # → True	True	OK	
print(array123([1, 1, 2, 4, 1])) # → False	False	OK	
print(array123([1, 1, 2, 1, 2, 3])) # → True	True	OK	
print(array123([1, 1, 2, 1, 2, 1])) # → False	False	OK	
print(array123([1, 2, 3, 1, 2, 3])) # → True	True	OK	
print(array123([1, 2, 3])) # → True	True	OK	
print(array123([1, 1, 1])) # → False	False	OK	
print(array123([1, 2])) # → False	False	OK	
print(array123([1])) # → False	False	OK	
print(array123([])) # → False	False	OK