file1 = open('film_titles.txt')

file2 = open('copy.txt', 'w')

file2.write(file1.read())
