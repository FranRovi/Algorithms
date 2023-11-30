# Leet Code Algo 2469. Convert the Temperature

def convertTheTemperature(celsius):
    # kelvin = celsius + 273.15
    # fahrenheit = celsius * 1.80 + 32.00
    # return [kelvin, fahrenheit]
    return [celsius + 273.15, celsius * 1.80 + 32.00]

print(convertTheTemperature(36.50))
print(convertTheTemperature(122.11)) 