import re
r = input('Input Regular Expression:\n> ')
string = input('Input String:\n> ')
result = bool(re.findall(r, string))
print(f"Input: '{r}|{string}'  Output: {result}")