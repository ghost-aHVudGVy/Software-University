budget = float(input())
video_cards = int(input())
processor = int(input())
ram = int(input())

video_card_cost = video_cards * 250
processor_1 = video_card_cost * 0.35
processor_cost = processor_1 * processor
ram_1 = video_card_cost * 0.1
ram_cost = ram_1 * ram
total_cost = video_card_cost + processor_cost + ram_cost

if video_cards > processor:
    total_cost *= 0.85
diff = abs(total_cost - budget)

if budget >= total_cost:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
