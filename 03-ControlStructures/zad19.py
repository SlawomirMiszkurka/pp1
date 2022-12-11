wiek = int(input('Podaj wiek psa'))
i = 0
psielata = 0
while i < wiek:
    if i < 2:
        psielata = psielata+10.5
    else:
        psielata = psielata+4
    i += 1
print(psielata)
