budget = int(input())
current_input = input()

while current_input != "End":
    current_item_price = int(current_input)
    budget -= current_item_price
    if budget < 0:
        print("You went in overdraft!")
        break
    current_input = input()
else:
    print("You bought everything needed.")
