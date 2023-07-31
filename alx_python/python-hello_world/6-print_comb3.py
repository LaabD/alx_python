for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        print(f"{tens_digit:02d}, {ones_digit:02d}", end=", ")

print()  # Print a new line after all combinations


