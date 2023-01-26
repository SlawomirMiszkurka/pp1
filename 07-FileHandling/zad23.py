import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
averageTemperature=0
for i in temperatures:
    averageTemperature+=int(i)
print(f'Average temperature = {averageTemperature/len(temperatures)}')