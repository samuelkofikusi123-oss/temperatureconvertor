temperature = float(input("Enter temperature: "))

unit = input("Enter the current unit ( C or F): ")

if unit == "C":
    temperature = (temperature * 9/5) + 32
    print(f"the temperature in Fahrenheit is {temperature} Fahrenheit")


elif unit == "F":
    temperature = (temperature - 32) * 5 / 9
    print(f"the temperature in Celsius is {temperature} degree Celsius")

else:
    print(f"{unit} is not a valid unit")

