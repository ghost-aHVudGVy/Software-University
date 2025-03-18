def get_pattern_type():
    print("\n🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

    while True:
        try:
            pattern_type = int(input("Enter the pattern number (1-8): "))
            if pattern_type in range(1, 9):
                return pattern_type
            else:
                print("❌ Invalid choice! Please enter a number between 1 and 8.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def get_pattern_character():
    char = input("Enter the character to use for the pattern (default '*'): ")
    return char if char else '*'


def get_size_or_rows(prompt):
    while True:
        try:
            size = int(input(prompt))
            if size > 0:
                return size
            else:
                print("❌ Please enter a positive integer.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def draw_right_angled_triangle(rows, char):
    for row in range(rows):
        print(char * (row + 1))


def draw_square_hollow_center(size, char):
    for row in range(size):
        for col in range(size):
            if row == 0 or row == size - 1 or col == 0 or col == size - 1:
                print(char, end='')
            else:
                print(' ', end='')
        print("")


def draw_diamond(rows, char):
    for row in range(rows):
        print(' ' * (rows - row - 1) + char * (2 * row + 1))
    for row in range(rows - 1, 0, -1):
        print(' ' * (rows - row) + char * (2 * row - 1))


def draw_left_angled_triangle(rows, char):
    for row in range(rows, 0, -1):
        print(char * row)


def draw_hollow_square(size, char):
    draw_square_hollow_center(size, char)


def draw_pyramid(rows, char):
    for row in range(rows):
        print(' ' * (rows - row - 1) + char * (2 * row + 1))


def draw_reverse_pyramid(rows, char):
    for row in range(rows, 0, -1):
        print(' ' * (rows - row) + char * (2 * row - 1))


def draw_rectangle_hollow_center(rows, cols, char):
    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                print(char, end='')
            else:
                print(' ', end='')
        print("")


def main():
    pattern_type = get_pattern_type()
    char = get_pattern_character()

    if pattern_type in [1, 3, 4, 6, 7]:
        rows = get_size_or_rows("Enter the number of rows: ")
        if pattern_type == 1:
            draw_right_angled_triangle(rows, char)
        elif pattern_type == 3:
            draw_diamond(rows, char)
        elif pattern_type == 4:
            draw_left_angled_triangle(rows, char)
        elif pattern_type == 6:
            draw_pyramid(rows, char)
        elif pattern_type == 7:
            draw_reverse_pyramid(rows, char)
    elif pattern_type in [2, 5]:
        size = get_size_or_rows("Enter the size of the square: ")
        if pattern_type == 2:
            draw_square_hollow_center(size, char)
        elif pattern_type == 5:
            draw_hollow_square(size, char)
    elif pattern_type == 8:
        rows = get_size_or_rows("Enter the number of rows: ")
        cols = get_size_or_rows("Enter the number of columns: ")
        draw_rectangle_hollow_center(rows, cols, char)

    print("\n✅ Pattern drawn successfully!")


if __name__ == "__main__":
    main()
