product = str(input())
city = str(input())
quantity = float(input())
cost = 0

match city:
    case "Sofia":
        if product == "coffee":
            cost = quantity * 0.50
        elif product == "water":
            cost = quantity * 0.80
        elif product == "beer":
            cost = quantity * 1.20
        elif product == "sweets":
            cost = quantity * 1.45
        elif product == "peanuts":
            cost = quantity * 1.60
    case "Plovdiv":
        if product == "coffee":
            cost = quantity * 0.40
        elif product == "water":
            cost = quantity * 0.70
        elif product == "beer":
            cost = quantity * 1.15
        elif product == "sweets":
            cost = quantity * 1.30
        elif product == "peanuts":
            cost = quantity * 1.50
    case "Varna":
        if product == "coffee":
            cost = quantity * 0.45
        elif product == "water":
            cost = quantity * 0.70
        elif product == "beer":
            cost = quantity * 1.10
        elif product == "sweets":
            cost = quantity * 1.35
        elif product == "peanuts":
            cost = quantity * 1.55

print(cost)
