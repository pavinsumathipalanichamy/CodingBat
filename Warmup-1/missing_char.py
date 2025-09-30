'''
Given a non-empty string and an int n, 
return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string 
(i.e. n will be in the range 0..len(str)-1 inclusive).
missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
'''

# Code
def missing_char(str, n):
    return str[:n] + str[n+1:]

print(missing_char('kitten', 1)) # → 'ktten' OK	
print(missing_char('kitten', 0)) # → 'itten' OK	
print(missing_char('kitten', 4)) # → 'kittn' OK	
print(missing_char('Hi', 0)) # → 'i' OK	
print(missing_char('Hi', 1)) # → 'H' OK	
print(missing_char('code', 0)) # → 'ode' OK	
print(missing_char('code', 1)) # → 'cde' OK	
print(missing_char('code', 2)) # → 'coe' OK	
print(missing_char('code', 3)) # → 'cod' OK	
print(missing_char('chocolate', 8)) # → 'chocolat' OK	