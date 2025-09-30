'''
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.
front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
'''

def front3(front):
    if len(front) < 3:
        return 3 * front
    return 3 * front[0:3] 

print(front3('Java')) # → 'JavJavJav' OK	
print(front3('Chocolate')) # → 'ChoChoCho' OK	
print(front3('abc')) # → 'abcabcabc' OK	
print(front3('abcXYZ')) # → 'abcabcabc' OK	
print(front3('ab')) # → 'ababab' OK	
print(front3('a')) # → 'aaa' OK	
print(front3('')) # → '' OK