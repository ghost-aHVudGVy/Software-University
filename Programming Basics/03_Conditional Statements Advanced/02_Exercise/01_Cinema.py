type = str(input())
l = int(input())
c = int(input())
price = 0

area = l * c

match type:
    case "Premiere":
        price = area * 12.00
    case "Normal":
        price = area * 7.50
    case "Discount":
        price = area * 5.00

print(f"{price:.2f} leva")
