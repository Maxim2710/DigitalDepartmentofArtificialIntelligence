def is_valid_sudoku(matrix):
    for row in matrix:
        if len(set(row)) != 9:
            return False

    for col in range(9):
        if len(set(matrix[row][col] for row in range(9))) != 9:
            return False

    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block = []
            for row in range(3):
                for col in range(3):
                    block.append(matrix[block_row + row][block_col + col])
            if len(set(block)) != 9:
                return False

    return True

matrix = [[int(i) for i in input()] for _ in range(9)]
print('YES' if is_valid_sudoku(matrix) else 'NO')
