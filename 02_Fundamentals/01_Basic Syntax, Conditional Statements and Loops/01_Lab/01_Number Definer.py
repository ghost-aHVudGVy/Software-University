number = float(input())

if number < 0:
    if number > -1:
        print("small negative")
    elif number < -1_000_000:
        print("large negative")
    else:
        print("negative")
elif number == 0:
    print("zero")
else:
    if number < 1:
        print("small positive")
    elif number > 1_000_000:
        print("large positive")
    else:
        print("positive")
