book = input()

current_input = input()
book_counter = 0

while current_input != "No More Books":
    book_counter += 1
    if current_input == book:
        print(f"You checked {book_counter - 1} books and found it.")
        break
    current_input = input()
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")
