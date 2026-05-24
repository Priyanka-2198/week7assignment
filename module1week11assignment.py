def convert_temp(c):
    return (c * 9/5) + 32

while True:
    celsius = input("Enter temperature in Celsius: ")

    if celsius.lower() == "exit":
        print("Program ended")
        break

    fahrenheit = convert_temp(float(celsius))

    print("Temperature in Fahrenheit:", fahrenheit)

# Assertions for testing
assert convert_temp(0) == 32
assert convert_temp(10) == 50
assert convert_temp(-40) == -40

print("Temperature conversion successful!")