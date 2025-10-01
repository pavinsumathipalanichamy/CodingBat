'''
Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.
near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''

# Code
def near_hundred(n):
  return abs(n-100) <= 10 or abs(n-200) <= 10

print(near_hundred(93)) # → True	True	OK	
print(near_hundred(90)) # → True	True	OK	
print(near_hundred(89)) # → False	False	OK	
print(near_hundred(110)) # → True	True	OK	
print(near_hundred(111)) # → False	False	OK	
print(near_hundred(121)) # → False	False	OK	
print(near_hundred(-101)) # → False	False	OK	
print(near_hundred(-209)) # → False	False	OK	
print(near_hundred(190)) # → True	True	OK	
print(near_hundred(209)) # → True	True	OK	
print(near_hundred(0)) # → False	False	OK	
print(near_hundred(5)) # → False	False	OK	
print(near_hundred(-50)) # → False	False	OK	
print(near_hundred(191)) # → True	True	OK	
print(near_hundred(189)) # → False	False	OK	
print(near_hundred(200)) # → True	True	OK	
print(near_hundred(210)) # → True	True	OK	
print(near_hundred(211)) # → False	False	OK	
print(near_hundred(290)) # → False	False	OK