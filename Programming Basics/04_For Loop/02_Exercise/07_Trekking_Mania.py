number_groups = int(input())

m1_people = 0
m2_people = 0
m3_people = 0
m4_people = 0
m5_people = 0
total_people = 0

for _ in range(number_groups):
    current_group_count = int(input())
    if current_group_count <= 5:
        m1_people += current_group_count
        total_people += current_group_count
    elif current_group_count <= 12:
        m2_people += current_group_count
        total_people += current_group_count
    elif current_group_count <= 25:
        m3_people += current_group_count
        total_people += current_group_count
    elif current_group_count <= 40:
        m4_people += current_group_count
        total_people += current_group_count
    else:
        m5_people += current_group_count
        total_people += current_group_count

m1 = m1_people / total_people * 100
m2 = m2_people / total_people * 100
m3 = m3_people / total_people * 100
m4 = m4_people / total_people * 100
m5 = m5_people / total_people * 100

print(f'{m1:.2f}%')
print(f'{m2:.2f}%')
print(f'{m3:.2f}%')
print(f'{m4:.2f}%')
print(f'{m5:.2f}%')
