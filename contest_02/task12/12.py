from collections import deque


def is_can_exit_from_maze(maze, start_row, start_col):
    rows = len(maze)
    cols = len(maze[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(start_row, start_col)])

    visited = [[False] * cols for _ in range(rows)]
    visited[start_row][start_col] = True

    while queue:
        row, col = queue.popleft()

        if maze[row][col] == 'E':
            return True

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                if maze[new_row][new_col] != '#':
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))

    return False


if __name__ == "__main__":
    start_row, start_col = [int(i) for i in input().split()]
    rows, cols = [int(i) for i in input().split()]
    maze = [list(input().strip()) for _ in range(rows)]

    print("YES" if is_can_exit_from_maze(maze, start_row, start_col) else "NO")
