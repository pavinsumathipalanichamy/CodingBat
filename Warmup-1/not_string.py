'''
Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.
not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
'''

# Code
def not_string(str):
    if str[:3] == 'not':
        return str
    else:
        return 'not ' + str

print(not_string('candy')) # → 'not candy' OK	
print(not_string('x')) # → 'not x' OK	
print(not_string('not bad')) # → 'not bad' OK	
print(not_string('bad')) # → 'not bad' OK	
print(not_string('not')) # → 'not' OK	
print(not_string('is not')) # → 'not is not' OK	
print(not_string('no')) # → 'not no' OK	