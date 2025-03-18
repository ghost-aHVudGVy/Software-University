city = str(input())
sales = float(input())
commission = 0
is_not_valid = False

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05 * sales
    elif 500 <= sales <= 1000:
        commission = 0.07 * sales
    elif 1000 <= sales <= 10000:
        commission = 0.08 * sales
    elif sales > 10000:
        commission = 0.12 * sales
    else:
        is_not_valid = True
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045 * sales
    elif 500 <= sales <= 1000:
        commission = 0.075 * sales
    elif 1000 <= sales <= 10000:
        commission = 0.1 * sales
    elif sales > 10000:
        commission = 0.13 * sales
    else:
        is_not_valid = True
        print("error")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055 * sales
    elif 500 <= sales <= 1000:
        commission = 0.08 * sales
    elif 1000 <= sales <= 10000:
        commission = 0.12 * sales
    elif sales > 10000:
        commission = 0.145 * sales
    else:
        is_not_valid = True
        print("error")
else:
    is_not_valid = True
    print("error")

if not is_not_valid:
    print(f"{commission:.2f}")
