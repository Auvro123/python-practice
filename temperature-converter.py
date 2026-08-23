def celsius_to_fahrenheit(c):
    return (c*9/5)+32

celsius=int(input('enter a input in celsius: '))
fahrenheit=celsius_to_fahrenheit(celsius)
print(fahrenheit)