day = str(input())
cost = 0

match day:
    case "Monday" | "Tuesday" | "Friday":
        cost = 12
    case "Wednesday" | "Thursday":
        cost = 14
    case "Saturday" | "Sunday":
        cost = 16

print(cost)
