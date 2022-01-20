def convert_to_fahrenheit(temp_degrees_celsius):
    temp_farenheit = (temp_degrees_celsius * 1.8) + 32
    return temp_farenheit

def convert_to_degrees_celsius(temp_farenheit):
    temp_degrees_celsius = (temp_farenheit -32)/ 1.8
    return  temp_degrees_celsius

print(convert_to_fahrenheit(24))
print(convert_to_degrees_celsius(75.2))