import re
with open('dummytext.txt') as file:
    words=re.findall('\w{6,}',file.read())
    for i in words:
        print(i,end="\n")