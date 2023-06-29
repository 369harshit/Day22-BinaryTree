def flood_fill(image, start_x, start_y, target_color, replacement_color):
    if image[start_x][start_y] == replacement_color:
        return

    rows = len(image)
    cols = len(image[0])

    def fill(x, y):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return

        if image[x][y] != target_color:
            return

        image[x][y] = replacement_color

        fill(x - 1, y)  # Check top neighbor
        fill(x + 1, y)  # Check bottom neighbor
        fill(x, y - 1)  # Check left neighbor
        fill(x, y + 1)  # Check right neighbor

    fill(start_x, start_y)


# Example usage
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

start_x = 1
start_y = 1

target_color = image[start_x][start_y]
replacement_color = 2

flood_fill(image, start_x, start_y, target_color, replacement_color)

# Print the filled image
for row in image:
    print(row)
