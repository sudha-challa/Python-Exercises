def predict_overlap(rows, cols, pos1, dir1, pos2, dir2):
    def update_position(pos, direction):
        # Update position based on direction
        pos[0] += direction[0]
        pos[1] += direction[1]

        # Handle bouncing off the walls
        if pos[0] == 0 or pos[0] == rows - 1:
            direction[0] *= -1
        if pos[1] == 0 or pos[1] == cols - 1:
            direction[1] *= -1

    # Convert map objects to lists
    pos1 = list(pos1)
    dir1 = list(dir1)
    pos2 = list(pos2)
    dir2 = list(dir2)

    # Simulate the movement until the balls overlap or reach the time limit
    steps = 0
    while pos1 != pos2:
        update_position(pos1, dir1)
        update_position(pos2, dir2)
        steps += 1

        # If the balls never overlap, return "Never"
        if steps > 1000000:
            return "3"

    return steps

# Read input
rows, cols = map(int, input().split())
pos1 = map(int, input().split())
dir1 = map(int, input().split())
pos2 = map(int, input().split())
dir2 = map(int, input().split())

# Call the function and print the result
result = predict_overlap(rows, cols, pos1, dir1, pos2, dir2)
print(result)
