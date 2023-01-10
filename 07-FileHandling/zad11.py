film_titles=['Spider Man','Harry Potter','Sparta','Minionki','Avatar']
file=open('film_titles.txt','w')
for i in film_titles:
    file.write(i)
    file.write('\n')