degrees = int(input())
time = str(input())
outfit = ""
shoes = ""

match time:
    case "Morning":
        if 10 <= degrees <= 18:
            outfit = "Sweatshirt"
            shoes = "Sneakers"
        elif 18 < degrees <= 24:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif degrees >= 25:
            outfit = "T-Shirt"
            shoes = "Sandals"
    case "Afternoon":
        if 10 <= degrees <= 18:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif 18 < degrees <= 24:
            outfit = "T-Shirt"
            shoes = "Sandals"
        elif degrees >= 25:
            outfit = "Swim Suit"
            shoes = "Barefoot"
    case "Evening":
        if 10 <= degrees <= 18:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif 18 < degrees <= 24:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif degrees >= 25:
            outfit = "Shirt"
            shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
