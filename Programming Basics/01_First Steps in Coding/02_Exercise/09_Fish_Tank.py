length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())

v = (length_cm * width_cm * height_cm) / 1000
v_taken = v * (percent / 100)
v_free = v - v_taken

print(v_free)
