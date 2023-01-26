import re
text='To be, or not to be, that is the question'
vowels=re.findall('a|e|i|o|u|y',text)
print(f'Number of vowels: {len(vowels)}')