def draw_pattern(size):
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1

def main():
    size = int(input("Enter the size of the pattern: "))
    while size <= 0:
        size = int(input("Please enter a positive integer: "))
    draw_pattern(size)

if __name__ == "__main__":
    main()
