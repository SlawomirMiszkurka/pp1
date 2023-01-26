import string

def f(first_letter, last_letter):
    count = 0
    with open("data.txt", encoding="utf8") as file:
        for line in file:
            for word in line.split():
                word = word.rstrip(string.punctuation)
                if word.startswith(first_letter) and word.endswith(last_letter):
                    count += 1
    return count
print(f("w","d"))