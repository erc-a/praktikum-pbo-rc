#triangle

def triangle(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

height = int(input("Height : "))
triangle(height)