days = int(input())
type_of_room = input()
rate = input()

price = 0
nights = days - 1
room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00

if days < 10:
    match type_of_room:
        case "room for one person":
            price = room_for_one_person * nights
        case "apartment":
            price = (apartment * nights) * 0.70
        case "president apartment":
            price = (president_apartment * nights) * 0.90
elif days <= 15:
    match type_of_room:
        case "room for one person":
            price = room_for_one_person * nights
        case "apartment":
            price = (apartment * nights) * 0.65
        case "president apartment":
            price = (president_apartment * nights) * 0.85
else:
    match type_of_room:
        case "room for one person":
            price = room_for_one_person * nights
        case "apartment":
            price = (apartment * nights) * 0.50
        case "president apartment":
            price = (president_apartment * nights) * 0.80

if rate == "positive":
    price *= 1.25
elif rate == "negative":
    price *= 0.90

print(f"{price:.2f}")
