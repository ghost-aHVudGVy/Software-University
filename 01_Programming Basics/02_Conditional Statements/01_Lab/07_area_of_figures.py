import math

figure = str(input())
area = 0;

if figure == "square":
    number_1 = float(input())
    area = number_1 * number_1
    print(area)
elif figure == "rectangle":
    number_1 = float(input())
    number_2 = float(input())
    area = number_1 * number_2
    print(area)
elif figure == "circle":
    number_1 = float(input())
    area = math.pi * number_1 ** 2
    print(area)
elif figure == "triangle":
    number_1 = float(input())
    number_2 = float(input())
    area = number_1 * number_2 / 2
    print(area)
