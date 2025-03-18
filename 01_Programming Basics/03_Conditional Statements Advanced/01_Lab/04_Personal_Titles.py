age = float(input())
gender = str(input())

match gender:
    case "m":
        if age < 16:
            print("Master")
        else:
            print("Mr.")
    case "f":
        if age < 16:
            print("Miss")
        else:
            print("Ms.")
