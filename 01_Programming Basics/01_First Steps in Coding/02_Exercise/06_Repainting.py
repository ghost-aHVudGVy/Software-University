nylon_amount_needed = int(input())
paint_amount_needed_in_liters = int(input())
amount_of_paint_thinner_in_liters = int(input())
hours_needed_to_finish = int(input())

total_paint_amount = paint_amount_needed_in_liters * 1.1
total_nylon_amount = nylon_amount_needed + 2

total_nylon_cost = total_nylon_amount * 1.50
total_paint_cost = total_paint_amount * 14.50
total_thinner_cost = amount_of_paint_thinner_in_liters * 5
cost = total_paint_cost + total_thinner_cost + total_nylon_cost + 0.40
work_cost = (cost * 0.3) * hours_needed_to_finish
cost += work_cost

print(cost)
