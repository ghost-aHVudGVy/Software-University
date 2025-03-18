pack_amount_for_pens = int(input())
pack_amount_for_markers = int(input())
liters_of_board_cleaner = int(input())
discount = int(input())

pen_cost = pack_amount_for_pens * 5.80
marker_cost = pack_amount_for_markers * 7.20
board_cleaner_cost = liters_of_board_cleaner * 1.20
total_without_discount = pen_cost + marker_cost + board_cleaner_cost

total_discount = total_without_discount * (discount / 100)
total_cost = total_without_discount - total_discount

print(total_cost)
