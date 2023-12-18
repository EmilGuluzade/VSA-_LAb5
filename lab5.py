import math

# Tənliyi təyin edən funksiya
def equation(x):
    return x**2 - math.log(x)

# Intervalın təyini
a = 1
b = 2

# Hesablama üçün tələb olunan dəqiqlik
tolerance = 1e-6

# Parçanı yarıya bölmə üsulu ilə kök təxmini
while (b - a) / 2 > tolerance:
    c = (a + b) / 2
    if equation(c) == 0:
        break
    elif equation(c) * equation(a) < 0:
        b = c
    else:
        a = c

# Nəticəni çap et
print("Tənliyin kökü:", c)
