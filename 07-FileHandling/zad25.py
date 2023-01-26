import re
text='To be, or not to be, that is the question'
words=re.findall('\w{1,}',text)
print(f'Number of words: {len(words)}')