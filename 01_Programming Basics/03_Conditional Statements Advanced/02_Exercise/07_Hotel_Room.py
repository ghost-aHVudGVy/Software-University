month = str(input())
nights = int(input())

apartment_cost = 0
studio_cost = 0

match month:
    case "May" | "October":
        apartment_cost = 65 * nights
        studio_cost = 50 * nights
    case "June" | "September":
        apartment_cost = 68.70 * nights
        studio_cost = 75.20 * nights
    case "July" | "August":
        apartment_cost = 77 * nights
        studio_cost = 76 * nights

if nights > 14 and (month == "May" or month == "October"):
    studio_cost *= 0.7
elif nights > 7 and (month == "May" or month == "October"):
    studio_cost *= 0.95
elif nights > 14 and (month == "June" or month == "September"):
    studio_cost *= 0.8

if nights > 14:
    apartment_cost *= 0.90

print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")
