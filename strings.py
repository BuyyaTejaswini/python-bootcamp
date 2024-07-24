#strings
'''
string methods are
is alpha
is digit
is alium
is upper
is lower
converting to lower
converting to upper
converting to swap
converting to title
'''

str="hellaa woRld"
print(str.lower())
print(str.strip())
print(str.upper())
print(str.swapcase())
print(str.title())
print(str.split())
print(str.replace('a','z'))
print(str.split('a'))

inp="hellaaaaa world"
print(inp.upper()) #to get upper char
print(inp.lower()) #to get lower char
print(inp.title()) #title means to get first letter capital
print(inp.swapcase()) #swap the upper to lower and vice versa
print(inp.strip()) #make space
print(inp.replace('a','z'))#replaces
print(inp.split()) #prints',' in space
print(inp.split('a')) #prints',' in given
#
inp="12"
print(inp.isalpha())# check space if space flase, if no space true
print(inp.isnumeric())#numeric are all numbers
print(inp.isascii())#whether input is ascii or not
print(inp.isalnum())
print(inp.isdigit())#digts are 0 to 9
print(inp.isupper())
print(inp.islower())
print(inp.istitle())
print(inp.isnumeric())
print(inp.isdigit())
