chicken_menu_amount = int(input())
fish_menu_amount = int(input())
vegetarian_menu_amount = int(input())

chicken_cost = chicken_menu_amount * 10.35
fish_cost = fish_menu_amount * 12.40
vegetarian_cost = vegetarian_menu_amount * 8.15
total = (chicken_cost + fish_cost + vegetarian_cost) * 1.2 + 2.5

print(total)
