'''
Given a non-empty string like "Code" return a string like "CCoCodCode".
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

# Code
def string_splosion(str):
  new_str = ''
  for i in range(len(str)+1):
    new_str += str[0:i]
  return new_str

print(string_splosion('Code')) # → 'CCoCodCode'	'CCoCodCode'	OK	
print(string_splosion('abc')) # → 'aababc'	'aababc'	OK	
print(string_splosion('ab')) # → 'aab'	'aab'	OK	
print(string_splosion('x')) # → 'x'	'x'	OK	
print(string_splosion('fade')) # → 'ffafadfade'	'ffafadfade'	OK	
print(string_splosion('There')) # → 'TThTheTherThere'	'TThTheTherThere'	OK	
print(string_splosion('Kitten')) # → 'KKiKitKittKitteKitten'	'KKiKitKittKitteKitten'	OK	
print(string_splosion('Bye')) # → 'BByBye'	'BByBye'	OK	
print(string_splosion('Good')) # → 'GGoGooGood'	'GGoGooGood'	OK	
print(string_splosion('Bad')) # → 'BBaBad'	'BBaBad'	OK