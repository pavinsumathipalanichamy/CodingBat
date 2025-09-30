'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
'''

# Code
def makes10(a, b):
    return a == 10 or b == 10 or a+b == 10

print(makes10(9, 10)) # → True OK	
print(makes10(9, 9)) # → False OK	
print(makes10(1, 9)) # → True OK	
print(makes10(10, 1)) # → True OK	
print(makes10(10, 10)) # → True	OK	
print(makes10(8, 2)) # → True OK	
print(makes10(8, 3)) # → False OK	
print(makes10(10, 42)) # → True	OK	
print(makes10(12, -2)) # → True	OK