'''
Given a string and a non-negative int n, 
return a larger string that is n copies of the original string.
string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''

def string_times(str, n):
    return str * n

print(string_times('Hi', 2)) # → 'HiHi'	'HiHi'	OK	
print(string_times('Hi', 3)) # → 'HiHiHi'	'HiHiHi'	OK	
print(string_times('Hi', 1)) # → 'Hi'	'Hi'	OK	
print(string_times('Hi', 0)) # → ''	''	OK	
print(string_times('Hi', 5)) # → 'HiHiHiHiHi'	'HiHiHiHiHi'	OK	
print(string_times('Oh Boy!', 2)) # → 'Oh Boy!Oh Boy!'	'Oh Boy!Oh Boy!'	OK	
print(string_times('x', 4)) # → 'xxxx'	'xxxx'	OK	
print(string_times('', 4)) # → ''	''	OK	
print(string_times('code', 2)) # → 'codecode'	'codecode'	OK	
print(string_times('code', 3)) # → 'codecodecode'	'codecodecode'	OK	