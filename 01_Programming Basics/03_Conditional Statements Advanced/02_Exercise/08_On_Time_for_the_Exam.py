h_exam = int(input())
m_exam = int(input())
h_arrived = int(input())
m_arrived = int(input())
late = False

# Convert exam time to minutes past midnight
exam_minutes = (h_exam * 60) + m_exam

# Convert arrival time to minutes past midnight
arrival_minutes = (h_arrived * 60) + m_arrived

# Calculate time difference in minutes
time_difference = abs(exam_minutes - arrival_minutes)

if exam_minutes < arrival_minutes:
    late = True
    print("Late")
elif exam_minutes >= arrival_minutes and time_difference <= 30:
    print("On time")
else:
    print("Early")

if not late:
    if time_difference < 60 and time_difference != 0:
        print(f"{time_difference} minutes before the start")
    elif time_difference >= 60:
        h = time_difference // 60
        m = time_difference % 60
        if m < 10:
            print(f"{h}:{m:02d} hours before the start")
        else:
            print(f"{h}:{m} hours before the start")
elif late:
    if time_difference < 60:
        print(f"{time_difference} minutes after the start")
    else:
        h = time_difference // 60
        m = time_difference % 60
        if m < 10:
            print(f"{h}:{m:02d} hours after the start")
        else:
            print(f"{h}:{m} hours after the start")
