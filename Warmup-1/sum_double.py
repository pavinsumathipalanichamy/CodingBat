'''
Given two int values, return their sum. 
Unless the two values are the same, then return double their sum.
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''

# Code
def sum_double(x, y):
    if x == y:
        return 2 * (x + y)
    return x + y

print(sum_double(1, 2)) # → 3 OK	
print(sum_double(3, 2)) # → 5 OK	
print(sum_double(2, 2)) # → 8 OK	
print(sum_double(-1, 0)) # → -1 OK	
print(sum_double(3, 3)) # → 12 OK	
print(sum_double(0, 0)) # → 0 OK	
print(sum_double(0, 1)) # → 1 OK	
print(sum_double(3, 4)) # → 7 OK	