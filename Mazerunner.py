from collections import deque

def is_valid_move(row, col, maze, visited, num_blocks_with_2):
    # Check if the move is within the bounds of the maze
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
        # Check if the block is not an obstacle and hasn't been visited
        if maze[row][col] != 1 and not visited[row][col]:
            # Check the number of blocks with value 2
            return maze[row][col] != 2 or num_blocks_with_2 < 2
    return False

def find_shortest_path(maze, start, target):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    queue = deque([(start[0], start[1], 0, 0)])  # (row, col, distance, num_blocks_with_2)

    while queue:
        row, col, distance, num_blocks_with_2 = queue.popleft()

        # Check if the current position is the target
        if (row, col) == target:
            return distance

        # Mark the current position as visited
        visited[row][col] = True

        # Explore the adjacent positions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the move is valid
            if is_valid_move(new_row, new_col, maze, visited, num_blocks_with_2):
                # Update the number of blocks with value 2 if the current block has it
                if maze[new_row][new_col] == 2:
                    new_num_blocks_with_2 = num_blocks_with_2 + 1
                else:
                    new_num_blocks_with_2 = num_blocks_with_2

                # Add the new position to the queue
                queue.append((new_row, new_col, distance + 1, new_num_blocks_with_2))

    return "STUCK"

# Input
R, C = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(R)]
start = tuple(map(int, input().split()))
target = tuple(map(int, input().split()))

# Output
result = find_shortest_path(maze, start, target)
print(result)
