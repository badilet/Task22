# Напишите функцию который будет конвертировать Фаренгейт в Цельсии и наоборот.

def convert_temp(scale = None, source_temp = None):
    if scale == "F":
        return 'C', (source_temp - 32.0) * (5.0/9.0)
    elif scale == "C":
        return 'F', (source_temp * (9.0/5.0)) + 32.0
    else:
        print("Needs to be (F) or (C)!")

scale = input("Select (F) or (C): " )
source_temp = int(input("What is the temperature: " ))
s, m = convert_temp(scale, source_temp)
print(source_temp, "degrees", scale, "is", m, "degrees", s)

# celcius = int(input("Celcius:"))
# fahrenheit = int(input("Fahrenheit:"))

# def temperature():
#     celcius = int(input("Celcius:"))
#     fahrenheit = int(input("Fahrenheit:"))
#
#     far_celc = (far - 32) * 5/9
#     celc_far = (celc * 1.8) + 32
#
# print(temperature(f" {far}", f"{celc}"))



