current_input = input()
total_ticket_counter = 0
student = 0
standard = 0
kid = 0

while current_input != "Finish":
    ticket_counter = 0
    movie_name = current_input
    free_seats = int(input())
    current_input = input()
    while current_input != "End":
        ticket = current_input
        total_ticket_counter += 1
        ticket_counter += 1
        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1
        if ticket_counter >= free_seats:
            break
        current_input = input()

    percent = ticket_counter / free_seats * 100
    print(f"{movie_name} - {percent:.2f}% full.")
    current_input = input()
student_percent = student / total_ticket_counter * 100
standard_percent = standard / total_ticket_counter * 100
kid_percent = kid / total_ticket_counter * 100
print(f"Total tickets: {total_ticket_counter}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
