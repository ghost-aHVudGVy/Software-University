fruit = str(input())
day = str(input())
quantity = float(input())
cost = 0
is_Valid = True

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        cost = quantity * 2.50
    elif fruit == "apple":
        cost = quantity * 1.20
    elif fruit == "orange":
        cost = quantity * 0.85
    elif fruit == "grapefruit":
        cost = quantity * 1.45
    elif fruit == "kiwi":
        cost = quantity * 2.70
    elif fruit == "pineapple":
        cost = quantity * 5.50
    elif fruit == "grapes":
        cost = quantity * 3.85
    else:
        is_Valid = False
        print("error")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        cost = quantity * 2.70
    elif fruit == "apple":
        cost = quantity * 1.25
    elif fruit == "orange":
        cost = quantity * 0.90
    elif fruit == "grapefruit":
        cost = quantity * 1.60
    elif fruit == "kiwi":
        cost = quantity * 3.00
    elif fruit == "pineapple":
        cost = quantity * 5.60
    elif fruit == "grapes":
        cost = quantity * 4.20
    else:
        is_valid = False
        print("error")
else:
    is_Valid = False
    print("error")

if is_Valid:
    print(f"{cost:.2f}")
