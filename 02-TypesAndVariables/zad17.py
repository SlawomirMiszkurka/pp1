print("Podaj swój wzrost")
x = int(input())
cale = x/2.54
print(f"Twój wzrost to", cale//12, "stóp i", round(cale % 12, 2), "cali")
