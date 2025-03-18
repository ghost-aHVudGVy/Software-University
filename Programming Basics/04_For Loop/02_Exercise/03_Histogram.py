n = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0

for _ in range(n):
    current_num = int(input())
    if current_num < 200:
        p1_counter += 1
    elif current_num <= 399:
        p2_counter += 1
    elif current_num <= 599:
        p3_counter += 1
    elif current_num <= 799:
        p4_counter += 1
    else:
        p5_counter += 1

p1 = p1_counter / n * 100
p2 = p2_counter / n * 100
p3 = p3_counter / n * 100
p4 = p4_counter / n * 100
p5 = p5_counter / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
