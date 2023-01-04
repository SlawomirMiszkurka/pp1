def count_letter(string, letter):
    counter = 0
    for i in string:
        if i == letter:
            counter += 1
    print(counter)


count_letter('You never get a second chance to make a first impression', 'a')
