'''
Given a string, return a new string where the first and last chars have been exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''

# Code
def front_back(str):
    if len(str) > 1:
        new_str = str[len(str)-1] + str[1:len(str)-1] + str[0]
    else:
        new_str = str
    return new_str

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
print(front_back('abc'))
print(front_back(''))
print(front_back('Chocolate'))
print(front_back('Java'))
print(front_back('hello'))