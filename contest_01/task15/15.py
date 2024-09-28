data = input().strip()

measurements = data.split(';')

temperatures = [int(temp) for temp in measurements if temp]

if temperatures:
    average_temperature = sum(temperatures) / len(temperatures)
else:
    average_temperature = 0.0

print(f"{average_temperature:.15f}")
