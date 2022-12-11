print("Podaj swój wzrost w cm")
wzrost = int(input())
print("Podaj swoją wagę")
waga = int(input())
bmi = waga/(wzrost/100)**2
print(f"Twoje BMI wynosi {bmi}")
