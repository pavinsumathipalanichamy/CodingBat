'''
Given a string, return a version without the first and last char, 
so "Hello" yields "ell". The string length will be at least 2.
without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
'''

# Code
def without_end(str):
    return str[1:-1]

print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))
print(without_end('code'))
print(without_end('ab'))
print(without_end('Chocolate!'))
print(without_end('kitten'))
print(without_end('woohoo'))
