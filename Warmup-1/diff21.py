'''
Given an int n, return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''

# Code
def diff21(n):
    if n > 21:
        return 2 * abs(n - 21)
    return abs(n - 21)

print(diff21(19)) # → 2	OK	
print(diff21(10)) # → 11 OK	
print(diff21(21)) # → 0	OK	
print(diff21(22)) # → 2	OK	
print(diff21(25)) # → 8	OK	
print(diff21(30)) # → 18 OK	
print(diff21(0)) # → 21	OK	
print(diff21(1)) # → 20	OK	
print(diff21(2)) # → 19	OK	
print(diff21(-1)) # → 22 OK	
print(diff21(-2)) # → 23 OK	
print(diff21(50)) # → 58 OK