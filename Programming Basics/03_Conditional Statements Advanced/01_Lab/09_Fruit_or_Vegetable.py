product = str(input())
is_unknown = True

match product:
    case "banana" | "apple" | "kiwi" | "cherry" | "lemon" | "grapes":
        is_unknown = False
        print("fruit")
    case "tomato" | "cucumber" | "pepper" | "carrot":
        is_unknown = False
        print("vegetable")

if is_unknown:
    print("unknown")
