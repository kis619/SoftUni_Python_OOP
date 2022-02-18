def print_a_row(size, star_count):
    spaces = size-star_count
    print(" " * spaces, end="")
    for i in range(1, star_count):
        print("*", end=" ")
    print("*")


size = int(input())
for star_count in range(1, size):
    print_a_row(size, star_count)
for star_count in range(size, 0, -1):
    print_a_row(size, star_count)