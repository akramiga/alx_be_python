FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return  (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    
    
def convert_to_fahrenheit(celsius):
    return  (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    

temperature = float(input("Enter the temperature to convert: "))
temp_value = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper() 
if temp_value == "F":
    cels = convert_to_celsius(temperature)
    print(f"{temperature}°{temp_value} is {cels}°C")
elif temp_value == "C":
    fahren = convert_to_fahrenheit(temperature)
    print(f"{temperature}°{temp_value} is {fahren}°F")  
else:
    print("Invalid temperature. Please enter a numeric value.")            